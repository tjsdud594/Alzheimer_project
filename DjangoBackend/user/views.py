from django.shortcuts import render
from django.views.generic import ListView
from django.db import models
from function.models import PredData
# Create your views here.
def user(request):
    context = {''}
    return render(request,'user/login.html', context)

class PostListView(ListView):
    template_name = "user/mypage.html"  #목록페이지 (응답페이지)
    model = PredData #데이터를 조회할 Model클래스
    paginate_by = 10 # 한번(한페이지)에 10개씩만 조회

