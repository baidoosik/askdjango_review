from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.conf import settings

urlpatterns =[
    url(r'^signup/$',views.signup_form,name='sign_up'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^login/$',login,name='login',kwargs={
        'template_name':'accounts/login.html'
        }),
    url(r'^logout/$',logout, name='logout',
            kwargs={'next_page': settings.LOGIN_URL}),
]