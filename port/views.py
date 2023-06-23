from django.shortcuts import render, redirect

from .forms import PortfolioForm, ProfileForm
#from django.contrib.auth.decorators import login_required #로그인 데코레이터
# Create your views here.
from .models import my_detail, Portfolio, Profile
from .models import user_detail

def index(request):
    return render(request, 'common/login.html')

def profile(request):
    return render(request, 'port/profile.html')

def my_Detail(request): #함수이름과 모델이름 구분해서 짓기
    detail = my_detail.objects.first()  
    return render(request, 'port/my_detail.html', {'my_detail': detail})

def user_Detail(request): #함수이름과 모델이름 구분해서 짓기
    detail = user_detail.objects.first()
    return render(request, 'port/user_detail.html', {'user_detail': detail})

def port_view(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('port:port_view')  # Redirect to the same page to display the updated contents
    else:
        form = PortfolioForm()

    portfolios = Portfolio.objects.all()  # Retrieve all objects from the database

    context = {
        'form': form,
        'portfolios': portfolios
    }

    return render(request, 'port/portfolio_list.html', context)


def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.all().delete()  # Delete all data in the database
            form.save()  # Save the form data to the database
            return redirect('port:profile_view')  # Redirect to the same page to display the updated contents
    else:
        form = ProfileForm()

    # Retrieve the profile object from the database (assuming there is only one)
    try:
        profile = Profile.objects.latest('id')
    except Profile.DoesNotExist:
        profile = None

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'port/profile_detail.html', context)