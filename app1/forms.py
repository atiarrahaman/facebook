from django import forms
from .models import Hunting



class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))
    class Meta:
        model=Hunting
        fields='__all__'
       