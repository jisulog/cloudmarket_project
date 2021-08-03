
from django.urls import path
from .views import post_views

# 이미지
# from django.conf.urls.static import static
# from django.conf import settings

# 네임스페이스 추가 - 박지수
app_name = 'market'


urlpatterns = [
    # post_views.py - 박지수
    path('', post_views.PostList.as_view(), name='postlist'),
    path('create/', post_views.PostCreate.as_view(), name = 'postcreate' ),
    path('<int:pk>/', post_views.PostDetail.as_view(), name = 'postdetail' ),
    path('update/<int:pk>/', post_views.PostUpdate.as_view(), name='postupdate'),
    path('delete/<int:pk>/', post_views.PostDelete.as_view(), name='postdelete'),
    #path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
]