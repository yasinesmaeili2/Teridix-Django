from django.shortcuts import redirect, render
from Teridix_main.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .forms import(
    SingupForm,
    SinginForm
)



def AccountView(request):

    blog = Blog.objects.all()
    c = {
        'posts':blog
    }
    return render(request,'View/accounts.html',c)



def LoginView(request):
    if request.user.is_authenticated:
        return redirect('Teridix_main:blog')
    else:
        form = SinginForm(request.POST or None)
        if form.is_valid():
            Username = form.cleaned_data.get('UserName')
            Password = form.cleaned_data.get('Password')
            user = authenticate(request,username=Username,password=Password)
            if user is not None:
                if user.is_superuser or user.is_auther:
                    login(request,user)
                    return redirect('Teridix_account:account')
                else:
                    login(request,user)
                    return redirect('Teridix_main:blog')
            else:
                form.add_error('UserName','نام کاربری یا رمز عبور اشتباه میباشد!')

        c = {
            'form':form
        }
    return render(request,'View/signin.html',c)


User = get_user_model()
def RegisterView(request):
    form = SingupForm(request.POST or None)
    if form.is_valid():
        Username = form.cleaned_data.get('UserName')
        Email = form.cleaned_data.get('Email')
        Password = form.cleaned_data.get('Password')
        User.objects.create_user(username=Username,email=Email,password=Password)
        user = authenticate(username=Username,password=Password)
        if user is not None:
            login(request,user)
            return redirect('Teridix_main:blog')

    c = {
        'form':form
    }
        
    return render(request,'View/signup.html',c)



def LogoutRequest(request):
    logout(request)
    return redirect('Teridix_main:blog')