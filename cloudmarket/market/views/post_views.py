from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from market.models import Post
from market.forms import CommentForm, PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# 시그널(이미지 삭제)
import os
from django.db import models
from django.dispatch import receiver
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator

# Create your views here.
# CBV(Class Based View) 사용하기

class PostList(ListView):
    paginate_by = 6
    # 자동: context = {'page_obj':page_obj}
    # 제네릭 뷰의 강력함 : 이 코드 한줄이면 뒤부턴 페이징을 신경쓸 필요가 없다
    #template_name = 'templates/market/post_list.html'
    global post_list
    def get_queryset(self):
        global post_list
        #page = self.request.GET.get('page','1') # paging 관련 코드가 필요가 없어짐
        kw = self.request.GET.get('kw','')
        post_list=Post.objects.order_by('-create_date')

        if kw:
            post_list = post_list.filter(
                Q(post_title__icontains=kw) |       # 제목검색
                Q(content__icontains=kw) |          # 내용검색
                Q(user_id__last_name__icontains=kw) #글쓴이 검색
            ).distinct()

        return post_list #return 타입 역시 queryset. 복잡하게 생각말기(render, reverse_lazy 필요없음)
      
        #subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.    
        #filter 함수에서 모델 속성에 접근하기 위해서는 이처럼 __ (언더바 두개) 를 이용하여 하위 속성에 접근할 수 있다.
    def get_context_data(self, *, object_list=None, **kwargs):
        context ={"kw" : self.request.GET.get('kw','')}
        kwargs.update(context)
        return super().get_context_data(**kwargs)

class PostDetail(DetailView):
    model = Post
    template_name = 'market/post_detail.html'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        # context['form'] = CommentForm(initial={'content': '',})
        context['form'] = CommentForm
        return context


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'market/post_create.html'
    success_url = reverse_lazy('market:postdetail')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user_id = self.request.user
        post.create_date = datetime.now()
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})


class PostUpdate(UpdateView):
    form_class = PostForm
    template_name = 'market/post_update.html'
    success_url = reverse_lazy('market:postdetail')

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post.modify_date = datetime.now()
        post.save()
        return post
    
    # 이미지 삭제
    @receiver(models.signals.pre_save, sender=Post)
    def auto_delete_file_on_change(sender, instance, **kwargs):
        if not instance.pk:
            return False
        try:
            old_file = Post.objects.get(pk=instance.pk).image
        except Post.DoesNotExist:
            return False
        new_file = instance.image
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})


class PostDelete(DeleteView):
    model = Post
    success_url = '/'

    # 이미지 삭제
    @receiver(models.signals.post_delete, sender=Post)
    def auto_delete_file_on_delete(sender, instance, **kwargs):
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

