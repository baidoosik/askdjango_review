from django import forms
from .models import Post,Comment
from review.widgets.naver_map_point_widget import NaverMapPointWidget


class PostModelForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['title','photo_thumbnail','content','tags','lnglat']
        widgets={
            'lnglat':NaverMapPointWidget(),
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
