from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed



def index(request):
    return HttpResponse("안녕하세요 portfolio site에 오신것을 환영합니다.")
