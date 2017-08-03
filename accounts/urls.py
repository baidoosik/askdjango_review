from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^signup/$',views.signup_form,name='sign_up'),
    url(r'^profile/(?P<id>\d+)/$',views.profile,name='profile'),
]