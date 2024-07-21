from django.shortcuts import render,redirect
from .forms import Loginform
# Create your views here.


def Login(request):
    if request.method =='POST':
        fm=Loginform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('https://www.facebook.com')
    else:
        fm=Loginform()
    context={'form':fm}
    return render (request,'login.html',context)



def Blog(request):
    return render(request,'blog.html')
