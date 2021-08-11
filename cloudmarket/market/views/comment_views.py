from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView
from market.models import Comment, Post
from market.forms import CommentForm
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
# CBV(Class Based View) 사용하기


class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = 'market/post_datail.html'
    success_url = reverse_lazy('market:postdetail')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post_id = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment.user_id = self.request.user
        comment.create_date = timezone.now()
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.post_id.pk}) 


class CommentUpdate(UpdateView):
    form_class = CommentForm
    template_name = 'market/post_detail.html'
    success_url = reverse_lazy('market:postdetail')

    def get_object(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        comment.modify_date = timezone.now()
        comment.save()
        return comment

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.post_id.pk})


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.post_id.pk}) 

#@login_required(login_url='common:login')
