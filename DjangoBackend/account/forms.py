from django import forms
from django.contrib.auth import get_user_model   # settings.py에 등록된 AUTH_USER_MODEL 클래스를 반환
from django.contrib.auth.models import User



# 회원가입할때 쓸 Form 정의
class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password확인', widget=forms.PasswordInput())
    # password1 = forms.CharField(label='Password')
    # password2 = forms.CharField(label='Password확인')
    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'password1', 'password2', 'hospital']

class LoginForm(forms.ModelForm):
    username = forms.EmailField(label='Email')
    # password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']