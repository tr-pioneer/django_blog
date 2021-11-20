from django import forms
from django.forms import fields
from .models import User
from django.contrib.auth.forms import UserCreationForm
# from django .core.exceptions import ValidationError 


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', "portfolio", "profile_pic", "first_name", "last_name")