from django.shortcuts import redirect, render
from Teridix_main.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .forms import SinginForm


@login_required
def AccountView(request):

    blog = Blog.objects.all()
    c = {
        'posts':blog
    }
    return render(request,'View/accounts.html',c)



def LoginView(request):
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