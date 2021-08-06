from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', login_views.CreateUserView.as_view(), name='signup'),
]