from django.urls import path

from . import views

app_name = 'port'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_detail/', views.my_detail, name='my_detail'),
    path('user_detail/', views.user_detail, name='user_detail'),
]