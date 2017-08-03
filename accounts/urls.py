from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns =[
    url(r'^signup/$',views.signup_form,name='sign_up'),
    url(r'^profile/(?P<id>\d+)/$',views.profile,name='profile'),
    url(r'^login/$',login,name='login',kwargs={
        'template_name':'accounts/login.html'
        }),
]