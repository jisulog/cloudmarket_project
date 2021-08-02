from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# 모델 추가 - 박지수
admin.site.register(Post)
admin.site.register(Comment)