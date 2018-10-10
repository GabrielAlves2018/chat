#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser, MensagemPV, Canal, Mensagem

# User: create
# - - - - - - - - - - - - - - - - - - -
class UUIDUserForm(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username', 'password')
        labels = {
        'username': 'Nome de Usuário',
        'password': 'Senha',
    }
        widgets={
            'password': forms.PasswordInput()
}

#User: edit
# - - - - - - - - - - - - - - - - - - -
class UUIDUserFormEdit(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username','password')
        labels = {
        'username': 'Nome de Usuário',
   }

#Canal
# - - - - - - - - - - - - - - - - - - -
class Canal(forms.ModelForm):
    class Meta:
        model = Canal
        fields = ('name', 'description')
        labels = {
        'name': 'Nome do Canal',
        'description': 'Mensagem',
        }

#Mensagem para conversa privada
# - - - - - - - - - - - - - - - - - - -
class MensagemPV(forms.ModelForm):
	class Meta:
		model = MensagemPV
		fields = ('recipient', 'message', 'thumbnail')
		label = {
		'recipient' : 'Destinatário',
		'message' : 'Escreva sua mensagem',
        'thumbnail' : 'Selecione uma imagem',
		}

#Mensagem do Canal
# - - - - - - - - - - - - - - - - - - -
class Mensagem(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ('channel', 'message', 'thumbnail')
        label = {
        'channel' : 'Canal',
        'message' : 'Escreva sua mensagem',
        'thumbnail' : 'Selecione uma imagem'
        }