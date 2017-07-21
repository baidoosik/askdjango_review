from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'add/(?P<x>\d*)/$',views.add_view,name='add'),
    url(r'add/(?P<x>\d*)/(?P<y>\d*)/$',views.add_view,name='add'),
    url(r'add/(?P<x>\d*)/(?P<y>\d*)/(?P<z>\d*)/$',views.add_view,name='add'),
]