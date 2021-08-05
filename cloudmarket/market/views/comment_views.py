from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from market.models import Comment
from market.forms import CommentForm
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
# CBV(Class Based View) 사용하기

class CommentCreate(CreateView, ):
    form_class = CommentForm
    template_name = 'market/comment_create.html'
    success_url = reverse_lazy('market:detail')

    def form_valid(self, post, form):
        post = get_object_or_404(Post, pk=post_id)
        comment = form.save(False)
        comment.create_date = timezone.now()
        comment.post = post
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('market:detail', kwargs={'pk':self.object.pk}) 
    
    # def commentcreate(request, post_id):
    #     post = get_object_or_404(Post, pk=post_id)
    #     post.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #     return redirect('market:detail', pk=post_id)
    

class CommentUpdate(UpdateView):
    form_class = CommentForm
    success_url = reverse_lazy('market:detail')

    def get_object(self):
        comment = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment.modify_date = timezone.now()
        comment.save()
        return post

    def get_success_url(self):
        return reverse_lazy('market:detail', kwargs={'pk':self.object.pk})


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.comment(request, *args, **kwargs)