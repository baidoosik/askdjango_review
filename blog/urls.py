from django.conf.urls import url,include
from django.contrib import admin
from . import views,cbv_views

urlpatterns =[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/detail/(?P<id>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/edit/(?P<id>\d+)/$',views.post_edit,name='post_edit'),
    url(r'^article/detail/(?P<id>\d+)/$',cbv_views.article_detail,name='article_detail'),
    # url(r'^post/(?P<id>\d+)/comment/new$',views.comment_new,name='comment_new'),
]