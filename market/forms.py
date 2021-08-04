from django import forms
from market.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'image', 'content', 'price']