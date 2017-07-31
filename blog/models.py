import re
from django.db import models
from django.forms import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',value):
        raise ValidationError('invalid lnglat information')

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #추상적인거 ...다른 모델에 공통적으로 쓰려고 만든거.

class Article(TimeStamp):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(TimeStamp):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=100, verbose_name='제목')
    photo_thumbnail = ProcessedImageField(
        upload_to='blog/post/%Y/%m/%d', processors=[Thumbnail(500,500 )],  # 처리할 작업목록
        format='JPEG',
        options={'quality': 60},
        blank=True)
    content = models.TextField(help_text='Markdown 문법을 적용해 주세요')
    tags = models.CharField(max_length=50,choices=(
        ('travel','travel'),
        ('sports','sports'),
        ('tech','tech'),
        ('coding','coding'),
    ),blank=True)
    lnglat = models.CharField(max_length=50,validators=[lnglat_validator],
                              help_text='경도,위도 포맷으로 입력해주세요.')

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    post =  models.ForeignKey(Post)
    author = models.CharField(max_length=40)
    message = models.TextField(max_length=100)
# Create your models here.
