from django.db import models
from django.urls.base import reverse

# Create your models here.

# 게시글 모델 - 박지수
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', max_length=300)
    content = models.TextField()
    price = models.IntegerField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

# 댓글 모델 - 박지수
class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)