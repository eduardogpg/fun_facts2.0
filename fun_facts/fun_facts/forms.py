#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User


"""
Constants
"""
ERROR_MESSAGE_USER = {'required' : 'El username es requerido', 'unique' : 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto' }
ERROR_MESSAGE_PASSWORD = {'required' : 'El password es requerido'} 
ERROR_MESSAGE_EMAIL = {'required' : 'El email es requerido', 'invalid': 'Ingrese un correo válido'}


class CreateUserForm(forms.ModelForm):
  username = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_USER  )
  password = forms.CharField(max_length=20, widget=forms.PasswordInput(), error_messages=ERROR_MESSAGE_PASSWORD)
  email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)

  class Meta:
    model = User
    fields = ('username', 'password', 'email')

class LoginForm(forms.Form):
  username = forms.CharField(max_length=20)
  password = forms.CharField(max_length=20, widget=forms.PasswordInput())
