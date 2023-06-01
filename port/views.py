from django.shortcuts import render
#from django.contrib.auth.decorators import login_required #로그인 데코레이터
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 port에 오신것을 환영합니다.")


def my_detail(request):
    return render(request, 'my_detail.html')

def user_detail(request):
    return render(request, 'user_detail.html')