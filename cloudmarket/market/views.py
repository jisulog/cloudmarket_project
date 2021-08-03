from django.views.generic import ListView
from .models import Post
from django.shortcuts import render , get_object_or_404, redirect
from django.utils import timezone


# Create your views here.
# CBV(Class Based View) 사용하기


def index(request):
    '''
    post 목록 출력
    '''
    post_list= Post.objects.order_by('-create_date')
    context ={'post_list' : post_list}
    return render(request, 'market/post_list.html', context)

def detail(request, post_id):
    """
    post 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'market/post_detail.html', context)

def comment_create(request, post_id):
    '''
    market 댓글 등록
    '''

    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('market:detail', post_id=post.id)

'''
class PostList(ListView):
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.order_by('-create_date')
'''