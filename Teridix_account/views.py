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
# for email
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


# sign up with send email verification
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
        # return redirect('Teridix_account:se')
        return HttpResponse('''
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <div id="main-wrapper">
            <div class="authincation section-padding">
                <div class="container ">
                    <div class="row justify-content-center h-100 align-items-center">
                        <div class="col-xl-5 col-md-6">
                            <div class="mini-logo text-center my-5">
                                <img src="images/logo.png" alt="">
                            </div>
                            <div class="auth-form card">
                                <div class="card-header justify-content-center text-center">
                                    <h4 class="card-title text-center">ایمیل فعالسازی</h4>
                                </div>
                                <div class="card-header text-center">
                                    <p class="text-center alert bg-success w-100 text-light">لینک فعال ساز برای شما ارسال شد لطفا ایمیلتان را چک کنید</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            
        ''')



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
        return HttpResponse('''
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <div id="main-wrapper">
            <div class="authincation section-padding">
                <div class="container ">
                    <div class="row justify-content-center h-100 align-items-center">
                        <div class="col-xl-5 col-md-6">
                            <div class="mini-logo text-center my-5">
                                <img src="images/logo.png" alt="">
                            </div>
                            <div class="auth-form card">
                                <div class="card-header text-center">
                                    <p class="text-center alert bg-success w-100 text-light">ایمیل شما با موفقیت ثبت شد و شما وارد شدید برای رفتن به صفحه اصلی <a class="text-warning" href="{% url 'Teridix_account:account %}">کلیک کنید</a></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        ''')
    else:
        return HttpResponse('''
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <div id="main-wrapper">
            <div class="authincation section-padding">
                <div class="container ">
                    <div class="row justify-content-center h-100 align-items-center">
                        <div class="col-xl-5 col-md-6">
                            <div class="mini-logo text-center my-5">
                                <img src="images/logo.png" alt="">
                            </div>
                            <div class="auth-form card">
                                <div class="card-header text-center">
                                    <p class="text-center alert bg-danger w-100 text-light">لینک فعال سازی منقضی شده است</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        ''')
# End sign-Up


