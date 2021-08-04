from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from market.models import Post
from market.forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# 시그널(이미지 삭제)
import os
from django.db import models
from django.dispatch import receiver

# Create your views here.
# CBV(Class Based View) 사용하기

class PostList(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.order_by('-create_date')

class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'market/post_create.html'
    success_url = reverse_lazy('market:postdetail')

    def form_valid(self, form):
        post = form.save(False)
        post.create_date = timezone.now()
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    form_class = PostForm
    template_name = 'market/post_update.html'
    success_url = reverse_lazy('market:postdetail')

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post.modify_date = timezone.now()
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