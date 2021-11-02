from django.shortcuts import render
# 언제 어떤 상황에서 데이터를 처리할지를 알려주는 파일
# 함수를 정의

def home(request): # request 가 들어오면
    return render(request, 'home/main.html')
