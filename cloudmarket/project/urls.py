
from django.contrib import admin
from django.urls import path, include
from market import views

urlpatterns = [
    # 홈 화면 추가 - 박지수
    #path('', views.PostList.as_view(), name="post"),
    path('admin/', admin.site.urls),
    # market app url 추가 - 박지수

    path('market/', include('market.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
