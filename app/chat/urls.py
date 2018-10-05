
from __future__ import unicode_literals

from django.urls import path, include
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chat'

urlpatterns = [
    #Home
     path('', views.Home.as_view(), name='home'),

     path('cadastro/', views.UserCreateView.as_view(), name='cadastro'),

     path('login/', auth_views.LoginView.as_view(template_name='auth.html'), name='login'),

     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
