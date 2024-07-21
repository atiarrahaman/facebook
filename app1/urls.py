from django.urls import path
from . import views

urlpatterns = [

    path('video',views.Login,name='video'),
    path('blog',views.Blog,name='blog'),
]
