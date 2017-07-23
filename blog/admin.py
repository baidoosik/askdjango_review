from django.contrib import admin
from .models import Post,Article

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','title']
    list_display_links = ['id','title']
    list_filter = ['author','tags']


@admin.register(Article)
class ArticlemodelAdmin(admin.ModelAdmin):
    list_display = ['id','title','url']
    list_display_links = ['id','title']

# Register your models here.
