
from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from datetime import datetime
from django.db import models


# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Canal(models.Model):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='canais', verbose_name='usuário')
    name = models.CharField(max_length=100, verbose_name='título')
    description = models.TextField(verbose_name='descrição')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'canal'
        verbose_name_plural = 'canais'

class Mensagem(models.Model):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='mensagens', verbose_name='usuário')
    channel = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='mensagens', verbose_name='canal')
    message = models.TextField(verbose_name='mensagens')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'mensagem'
        verbose_name_plural = 'mensagens'

class MensagemPV(models.Model):
    sender = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='mensagemsender', verbose_name='remetente')
    recipient = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='mensagemrecipient', verbose_name='destinatário')
    message = models.TextField(verbose_name='mensagempv')
    

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'mensagemPV'
        verbose_name_plural = 'mensagensPV'