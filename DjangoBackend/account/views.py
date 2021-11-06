from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import CustomUser

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm   # 로그인 Form: username, password

from .forms import UserForm, LoginForm

import time
import json

# Create your views here.

# class UserCreateView(CreateView):
#     template_name = 'account/join.html'  # GET 요청 -> 가입폼 template
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')   # POST요청 -> 가입처리 -> 성공후에 redirect 방식으로 이동할 url

# # 로그인 처리 View
# class UserLoginView(LoginView):
#     template_name = 'account/login.html'   # GET: 로그인 Form template
#     form_class = AuthenticationForm
#     # POST: 로그인 처리 - 성공 -> settings.py : LOGIN_REDIRECT_URL에 설정된 url로 이동(redirect)

# # 로그아웃 처리 view - LogoutView 사용  => 추가적으로 정의할 것이 없다
#     #    =>urls.py에 직접 등록
# class UserLogoutView(LogoutView):
#     pass

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            if request.POST['password1']==request.POST['password2']:

                context = {
                    'email' : request.POST['email'],
                    'name' : request.POST['name'],
                    'username' : request.POST['email'],
                    'password' : request.POST['password1'],
                    'hospital' : request.POST['hospital']
                }

                # 입력한 폼으로 로그인
                # auth.login(request, user)
                print('---------------------------------------------정상적으로 약관동의로 넘어감')
                return render(request, 'account/agreement.html', {'object' : context})

            else:
                print(1)
                context = {"message" : "비밀번호가 일치하지 않습니다."}
                return render(request, 'account/login.html', {"message" : "비밀번호가 일치하지 않습니다."})

        else:
            try:
                CustomUser.objects.get(email=request.POST['email'])
                print(1.5)
                return render(request, 'account/login.html', {"message" : "이미 가입된 이메일입니다"})
            except:
                print(2)
                context = {"message" : "이메일 양식이 올바르지 않습니다."}
                return render(request, 'account/login.html', {"message" : "이메일 양식이 올바르지 않습니다."})
    else:
        print(3)
        context = {"message" : "Wrong Mathod"}
        return render(request, "account/login.html", {"message" : "Wrong Mathod"})


def check_agreement(request):
    print('-----------------------------------check_agreement실행')

    try:
        user_agreement3=request.POST['agreement3']
        print(user_agreement3)
        user = CustomUser.objects.create_user(
                    username=request.POST['email'],
                    email=request.POST['email'],
                    name=request.POST['name'],
                    password=request.POST['password'],
                    hospital=request.POST['hospital'],
                    agreement1=True,
                    agreement2=True,
                    agreement3=True,
                )
        auth.login(request, user)
        print('-----------------------전부 동의한 사람!! 가입완료')
        return render(request, 'home/main.html', {"object" : user, "message" : "회원가입을 축하드립니다"})

   
    except:
        try:
            print('---------------------------------------프로모션 안사요')
            request.POST['agreement1'] 
            request.POST['agreement2']
            user = CustomUser.objects.create_user(
                        username=request.POST['email'],
                        email=request.POST['email'],
                        name=request.POST['name'],
                        password=request.POST['password'],
                        hospital=request.POST['hospital'],
                        agreement1=True,
                        agreement2=True,
                    )
            print('-----------------------광고 미동의')
            auth.login(request, user)
            return render(request, 'home/main.html', {"object": user, "message" : "회원가입을 축하드립니다"})

        except:
            return render(request, 'home/main.html', {"message" : "회원가입이 취소되었습니다."})
        
