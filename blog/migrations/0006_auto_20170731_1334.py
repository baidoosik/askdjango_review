# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-31 13:34
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_photo_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
