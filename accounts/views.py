from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserModelform
from .models import Profile,CustomUser

# Create your views here.

def signup_form(request):
    if request.method == 'POST':
        form = CustomUserModelform(request.POST,request.FILES)

        if form.is_valid():
            custom_user = form.save(commit=True)

            return redirect('accounts/profile')
        else:
            raise form.add_error('가입 형식이 올바르지 않습니다.')

    else:
        form = CustomUserModelform()

    return render(request,'accounts/signup_form.html',{
        'form':form
    })


def profile(request,id):
    my_profile = get_object_or_404(Profile)
    return render(request,'accounts/profile.html',{
        'profile':my_profile
    })