from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

class CustomUserModelform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =['username','profile_photo','email','birthday']

 