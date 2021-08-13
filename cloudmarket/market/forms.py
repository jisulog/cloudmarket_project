from django import forms
from market.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'image', 'price', 'content']
                
        labels = {
            'post_title' : '글 제목',
            'image': '파일선택',
            'price' : '가격',
            'content': '글 내용'
        }  
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
          'content': forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'cols':10}),
        }

        labels = {
            'content': '댓글 수정 중...',
        }  
