from django import forms
from market.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'image', 'content', 'price']

        widgets = {
          'post_title': forms.TextInput(attrs={'class': 'form-control'}),
          'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        
        labels = {
            'image': '첨부파일',
            'content': '내용',
            'price' : '가격'
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
