#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser, MensagemPV, Canal, Mensagem

# User: create
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

class UUIDUserFormEdit(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username','password')
        labels = {
        'username': 'Nome de Usuário',
   }

class Canal(forms.ModelForm):
    class Meta:
        model = Canal
        fields = ('name', 'description')
        labels = {
        'name': 'Nome do Canal',
        'description': 'Mensagem',
        }

class MensagemPV(forms.ModelForm):
	class Meta:
		model = MensagemPV
		fields = ('recipient', 'message')
		label = {
		'recipient' : 'Destinatário',
		'message' : 'Escreva sua mensagem',
		}

class Mensagem(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ('channel', 'message')
        label = {
        'channel' : 'Canal',
        'message' : 'Escreva sua mensagem',
        }