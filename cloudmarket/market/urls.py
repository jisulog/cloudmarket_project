"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import post_views, comment_views

# 이미지
# from django.conf.urls.static import static
# from django.conf import settings


app_name = 'market'


urlpatterns = [

    path('', post_views.PostList.as_view(), name='postlist'),
    path('<int:pk>/', post_views.PostDetail.as_view(), name = 'postdetail' ),

    path('post/create/', post_views.PostCreate.as_view(), name = 'postcreate' ),
    path('post/update/<int:pk>/', post_views.PostUpdate.as_view(), name='postupdate'),
    path('post/delete/<int:pk>/', post_views.PostDelete.as_view(), name='postdelete'),

    path('comment/create/<int:pk>/', comment_views.CommentCreate.as_view(), name='commentcreate'),
    path('comment/update/<int:pk>/', comment_views.CommentUpdate.as_view(), name='commentupdate'),
    path('comment/delete/<int:pk>/', comment_views.CommentDelete.as_view(), name='commentdelete'),
]