from django import forms
from .models import CustomUser

class CustomUserModelform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields =['username','password','profile_photo','email','birthday']