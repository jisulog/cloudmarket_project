from django.db import models
from django.urls.base import reverse
from imagekit.models import ProcessedImageField #resize
from imagekit.processors import ResizeToFit #resize
from django.contrib.auth.models import User
# Create your models here.

# 게시글 모델
class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid_post')
    post_title = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='img/', max_length=300)
    image = ProcessedImageField(upload_to='img/', processors=[ResizeToFit(500,500)]) #resize
    content = models.TextField()
    price = models.IntegerField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

# 댓글 모델
class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid_comment')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content
