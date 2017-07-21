from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','title']
    list_display_links = ['id','title']
    list_filter = ['author','tags']

# Register your models here.
