from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(User):
    # 추가필드
    profile_photo = ProcessedImageField(verbose_name='프로필 사진',
        upload_to='blog/post/%Y/%m/%d', processors=[Thumbnail(500,500 )],  # 처리할 작업목록
        format='JPEG',
        options={'quality': 60},
        blank=True)
    phone_num = PhoneNumberField(help_text='핸드폰 번호를 입력해 주세요.')



class Profile(models.Model):
    user = models.OneToOneField(CustomUser)

