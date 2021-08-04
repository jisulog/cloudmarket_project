from django.contrib import admin
from .models import Post, Comment#, User

# Register your models here.

#class UserAdmin(admin.ModelAdmin):
#    search_fields = ['username']

# 모델 추가 - 박지수
admin.site.register(Post)
admin.site.register(Comment)
#admin.site.register(User, UserAdmin)