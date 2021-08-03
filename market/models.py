from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
# Create your models here.

# 유저 모델
'''
class User(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.username
'''


# 게시글 모델 - 박지수
class Post(models.Model):
    used_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid_post')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_post')
    post_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', max_length=300)
    content = models.TextField()
    price = models.IntegerField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.post_title

# 댓글 모델 - 박지수
class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    used_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid_comment', null=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_comment')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)