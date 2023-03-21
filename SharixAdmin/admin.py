# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from SharixAdmin.models import *
from django import forms
from xmpp import cli
from django.contrib.auth.admin import UserAdmin
import django.contrib.auth.admin as adm

class MessageForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(label='Message', max_length=1000)


#@admin.action(description='Отправить сообщение на номер телефона')
def send_phone(modeladmin, request, queryset):
    form = None
    #print("Hello world")
    if 'apply' in request.POST:
        #print("Hello world")
        modeladmin.message_user(request, "Сообщения успешно отправлены!")
        form = MessageForm(request.POST)
        if form.is_valid():
            for i in queryset:
                if str(i.phone_number).startswith("7"):
                    message = '{"phone":"+'+i.phone_number+'","msg":"'+request.POST['message']+'"}'      
                else:
                    message = '{"phone":"'+i.phone_number+'","msg":"'+request.POST['message']+'"}'
                cli.send_message("sender", "password", "getter", message)
                print(i)
            print(request.POST['message'])
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = MessageForm(initial={'_selected_action': request.POST.getlist("_selected_action")})
           
    return render(request, "SharixAdmin/senderform.html", {"items":queryset, "form":form, 'title':'Отправка сообщений на номер телефона'})
send_phone.short_description = u"Отправить сообщение на номер телефона"

    
@admin.register(SharixUser)
class SharixUserAdmin(adm.UserAdmin):
    list_display = (
        'username',
        'phone_number',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    fieldsets = (
        ("Главное", {'fields': ('phone_number', 'password')}),
        ('Персональные данные', {'fields': (('username', 'email'), ('first_name','last_name'))}),
        ('Разрешения', {'fields': (('is_staff', 'is_active', 'is_superuser'),)}),
        ('Прочие разрешения', {'fields': ('groups', 'user_permissions'), 'classes': ['collapse']}),
        ('Прочее', {'fields': (('last_login', 'date_joined'),)}),
    )
    add_fieldsets = (
        ("Главное", {'fields': ('phone_number', 'password1', 'password2')}),
        ('Персональные данные', {'fields': (('username', 'email'), ('first_name','last_name'))}),
        ('Разрешения', {'fields': (('is_staff', 'is_active', 'is_superuser'),)}),
        ('Прочие разрешения', {'fields': ('groups', 'user_permissions'), 'classes': ['collapse']}),
        ('Прочее', {'fields': (('last_login', 'date_joined'),)}),
    )
    #raw_id_fields = ('groups', 'user_permissions')
    actions = [send_phone]

#admin.site.register(SharixUser, UserAdmin)