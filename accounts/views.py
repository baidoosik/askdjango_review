from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserModelform
from .models import Profile,CustomUser

# Create your views here.

def signup_form(request):
    if request.method == 'POST':
        form = CustomUserModelform(request.POST,request.FILES)

        if form.is_valid():
           form.save()

        return redirect('accounts:login')

    else:
        form = CustomUserModelform()

    return render(request,'accounts/signup_form.html',{
        'form':form
    })


def profile(request):
    my_profile = CustomUser.objects.filter(username=request.user).first()

    return render(request,'accounts/profile.html',{
        'profile':my_profile
    })