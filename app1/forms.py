from django import forms
from .models import Hunting



class Loginform(forms.ModelForm):
    username=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Email or phone number'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'type': 'password','placeholder':'Password'}))
    class Meta:
        model=Hunting
        fields='__all__'
       