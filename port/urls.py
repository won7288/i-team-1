from django.urls import path
from . import views

app_name = 'port'

urlpatterns = [
    path('', views.index, name='index'),
    path('MyPort_details/<int:MyPort_details_id>/', views.MyPort_details, name='MyPort_details'), #상세보기 URL매핑
]