from pyexpat import model
import re
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Teridix_main.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .mixins import (
    FieldMixin,
    FormValidMixin,
    AccessBlogMixin,
    SuperuserAccessMixin,
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .forms import(
    SingupForm,
    SinginForm,
    ProfileForm
)
from .models import User



def AccountView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            blog = Blog.objects.all()

        else:
            blog = Blog.objects.filter(author=request.user)
    else:
        return redirect('Teridix_account:login')

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



# User = get_user_model()
# def RegisterView(request):
#     if request.user.is_authenticated:
#         return redirect('Teridix_main:blog')
#     else:
#         form = SingupForm(request.POST or None)
#         if form.is_valid():
#             Username = form.cleaned_data.get('UserName')
#             Email = form.cleaned_data.get('Email')
#             Password = form.cleaned_data.get('Password')
#             User.objects.create_user(username=Username,email=Email,password=Password)
#             user = authenticate(username=Username,password=Password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('Teridix_main:blog')
# 
#         c = {
#             'form':form
#         }
#     return render(request,'View/signup.html',c)



def LogoutRequest(request):
    logout(request)
    return redirect('Teridix_main:blog')



# CRUD with class base

class Updating(AccessBlogMixin,FieldMixin,UpdateView):
    model = Blog
    template_name = 'View/createView.html'



class Creating(FormValidMixin,FieldMixin,CreateView):
    model = Blog
    template_name = 'View/createView.html'


class Deleting(SuperuserAccessMixin,DeleteView):
    model = Blog
    template_name = 'View/delete.html'
    success_url = reverse_lazy('Teridix_account:account')
    context_object_name = 'post'


class Profile(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('Teridix_account:account')
    template_name = 'View/profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)    
    
    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user
        })
        return kwargs





from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage



class Signup(CreateView):
    template_name = 'View/signup.html'
    form_class = SingupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('View/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد')




def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse("اکانت شما با موفقیت فعال شد")
    else:
        return HttpResponse('لینک فعال سازی منقضی شده است! لطفا دوباره تلاش کنید')