from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'function/function.html')

def result(request):
    return render(request, 'function/result.html')