from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from market.models import Post
from market.forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages

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
        post = form.save(commit=False)
        post.user_id = self.request.user
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
        if self.request.user != post.user_id:
            messages.error(self.request, '수정권한이 없습니다')
            return reverse_lazy('market:postlist')
        post.modify_date = timezone.now()
        post.save()
        return post

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})


class PostDelete(DeleteView):
    model = Post
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



'''
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from market.models import Post
from market.forms import PostForm
from django.utils import timezone

# Create your views here.
# CBV(Class Based View) 사용하기




class PostList(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.order_by('-create_date')

class PostCreate(CreateView):
    template_name = 'market/post_create.html'
    form_class = PostForm

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('market:postlist')
        else:
            form = PostForm()
        return render(request, 'market/post_create.html', {'form':form})

class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()

class PostUpdate(ListView):
    pass

class PostDelete(ListView):
    pass
'''