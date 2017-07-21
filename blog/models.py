from django.db import models
from django.forms import ValidationError
import re


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',value):
        raise ValidationError('invalid lnglat information')

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #추상적인거 ...다른 모델에 공통적으로 쓰려고 만든거.

class Post(TimeStamp):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 적용해 주세요')
    tags = models.CharField(max_length=100,blank=True)
    lnglat = models.CharField(max_length=50,validators=[lnglat_validator],
                              help_text='경도,위도 포맷으로 입력해주세요.')

# Create your models here.
