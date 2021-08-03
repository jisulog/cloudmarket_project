
from django.urls import path
from market import views

# 이미지
from django.conf.urls.static import static
from django.conf import settings

# 네임스페이스 추가 - 박지수
app_name = 'market'


urlpatterns = [
     path('',views.index, name='index'),
     path('<int:post_id>/', views.detail, name='detail'),
     path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    #path('', views.PostList.as_view(), name="post"),
]