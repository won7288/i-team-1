from django import forms
from .models import Portfolio, Profile

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['image', 'title', 'rating', 'content']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'header', 'career']