from django.shortcuts import render
from django.views.generic import ListView
from django.db import models
from function.models import PredData
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
def user(request):
    context = {''}
    return render(request,'user/login.html', context)

def board_detail(request, pk):
    board = PredData.objects.get(pk=pk)
    # pk 에 해당하는 글을 가지고 올 수 있게 된다.
    return render(request, 'user/board_detail.html', {'board':board})  

@method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    template_name = "user/mypage.html"  #목록페이지 (응답페이지)
    model = PredData #데이터를 조회할 Model클래스
    # django는 자동으로 연결한 DB의 정보가 object_list라는 이름으로 넘어감.

    def get_success_url(self):
        return reverse_lazy('board:detail', args=[self.object.pk])
    
    
