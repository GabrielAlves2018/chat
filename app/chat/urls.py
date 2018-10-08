
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

     path('chatpv/', views.Chatpv.as_view(), name='chatpv'),
     #Inside chatpv:
     path('mensagempv/', views.Mensagempv.as_view(), name='mensagempv'),

     path('vermsnpv/', views.Vermsnpv.as_view(), name='vermsnpv'),

     path('verhistorico/', views.Verhistorico.as_view(), name='verhistorico'),

     path('msnedit/<pk>/', views.Msnedit.as_view(), name='msnedit'),

     path('msndelete/<pk>/', views.Msndelete.as_view(), name='msndelete'),
     #Perfil
     path('perfil/', views.Perfil.as_view(), name='perfil'),

     path('perfiledit/<pk>/', views.Perfiledit.as_view(), name='perfiledit'),

     path('perfildelete/<pk>/', views.Perfildelete.as_view(), name='perfildelete'),

     path('listacanais/', views.ListaCanais.as_view(),name='listacanais'),

     path('canaldetail/<pk>/', views.CanalDetail.as_view(), name='canaldetail'),

     path('canalcreate/', views.CanalCreate.as_view(), name='canalcreate'),

     path('mychannels/', views.MyChannels.as_view(), name='mychannels'),

     path('editchannel/<pk>/', views.EditChannel.as_view(), name='editchannel'),

     path('removechannel/<pk>/', views.RemoveChannel.as_view(), name='removechannel'),

     path('mensagemcanal/', views.MensagemCanal.as_view(), name='mensagemcanal'),


]