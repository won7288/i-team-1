from django.urls import path

from . import views

app_name = 'port'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_detail/', views.my_detail, name='my_detail'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('edit/portfolio/', views.port_view, name='port_view'),
    # TBD: path('edit/profile', views.profile_view, name="profile_view")
]