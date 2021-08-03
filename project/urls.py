
from django.contrib import admin
from django.urls import path, include
from market.views import post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 홈 화면 추가 - 박지수
    #path('', views.PostList.as_view(), name="post"),
    path('admin/', admin.site.urls),
    # market app url 추가 - 박지수

    path('market/', include('market.urls')),
    path('', post_views.PostList.as_view(), name='postlist'),
    path('common/', include('common.urls')),
    #path('', views.index, name='index'),  # '/' 에 해당되는 path
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

