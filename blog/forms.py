from django import forms
from .models import *

class PostModelForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['title','photo_thumbnail','content','tags','lnglat']