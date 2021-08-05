from django import forms
from market.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'image', 'content', 'price']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']