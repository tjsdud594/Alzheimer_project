from django.urls import path

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView  # 로그인 Form: username, password

# from .forms import CustomUserCreationForm

from . import views
from .forms import LoginForm

app_name = 'account'

urlpatterns = [
    path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('agreement', views.signup, name='agreement'),
    path('check', views.check_agreement, name='check'),
    # path('logincheck', LoginView.as_view(template_name='home/main.html', form_class=AuthenticationForm), name='logincheck'),
    path('logincheck', LoginView.as_view(template_name='home/main.html', form_class=AuthenticationForm), name='logincheck'),
    path('logout', LogoutView.as_view(), name='logout'),  # 로그아웃처리
]