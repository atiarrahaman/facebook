from django.urls import path
from . import views

urlpatterns = [

    path('login',views.Login,name='login'),
    path('blog',views.Blog,name='blog'),
]
