# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import UUIDUser, Canal, Mensagem, MensagemPV


# UserAdmin
# - - - - - - - - - - - - - - - - - - -
class UserAdmin(auth.UserAdmin):

    fieldsets = (
        ('Personal info', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')

# Register
# - - - - - - - - - - - - - - - - - - -
admin.site.register(UUIDUser, UserAdmin)

#Meus Models
admin.site.register(Canal)
admin.site.register(Mensagem)
admin.site.register(MensagemPV) 