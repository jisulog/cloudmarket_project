
from django.contrib import admin
from django.urls import path, include
from market.views import post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # market app url 추가 - 박지수

    path('market/', include('market.urls')),
    path('common/', include('common.urls')),
    path('', post_views.PostList.as_view(), name='postlist'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

