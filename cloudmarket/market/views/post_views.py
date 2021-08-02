from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from market.models import Post
from market.forms import PostForm
from django.utils import timezone

# Create your views here.
# CBV(Class Based View) 사용하기

class PostList(ListView):
    paginate_by = 10
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