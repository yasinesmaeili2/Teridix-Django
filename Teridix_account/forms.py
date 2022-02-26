from django import forms
from django.core import validators
from django.contrib.auth import get_user_model
from .models import User as U
from django.contrib.auth.forms import UserCreationForm



User = get_user_model()

class SingupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = U
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'نام خودرا وارد کنید'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'ایمیل خودرا وارد کنید'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'گذروازه را وارد کنید'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'تایید گذرواژه'})

    def clean_UserName(self):
        Username = self.cleaned_data.get('UserName')
        filtering = User.objects.filter(username=Username)
        if filtering.exists():
            raise forms.ValidationError('این نام کاربری وجود دارد')
        return Username

    def clean_Email(self):
        Email = self.cleaned_data.get('Email')
        filtering = User.objects.filter(email=Email)
        if filtering.exists():
            raise forms.ValidationError('با این ایمیل قبلا ثبت نام شده است')
        return Email

    def clean_Confirm_Password(self):
        data = self.cleaned_data
        p1 = self.cleaned_data.get('Password')
        p2 = self.cleaned_data.get('Confirm_Password')

        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('رمز عبور فرق میکند')
            if len(p1) < 8:
                raise forms.ValidationError('رمز عبور نباید کمتر از 8 کاراکتر باشد')
        return data



class SinginForm(forms.Form):
    UserName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خودرا وارد کنید...'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز خودرا وارد کنید...'}))



class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)

        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['username'].help_text = '<p class="text-danger">شما نمیتوانید نام خودرا تغییر دهید!</p>'
            # self.fields['email'].disabled = True
            # self.fields['email'].help_text = '<p class="text-danger">شما نمیتوانید ایمیل خودرا تغییر دهید!</p>'
        self.fields['first_name'].help_text = '<p class="text-success"> نام خودرا میتوانید تغییر دهید</p>'
        self.fields['last_name'].help_text = '<p class="text-success">  نام خانوادگی خودرا میتوانید  تغییر دهید</p>'

    class Meta:
        model = U
        fields = ['username','email','first_name','last_name','is_auther','image']





# Sign-Up Normal        
# class SingupForm(forms.Form):
#     UserName = forms.CharField(widget=forms.TextInput(
#         attrs={'class':'form-control','placeholder':'نام کاربری'}
#         ),validators=[
#             validators.MaxLengthValidator(limit_value=20,message='نام کاربری نمیتواند بیشتر از 20 کاراکتر باشد'),
#             validators.MinLengthValidator(limit_value=4,message='نام کاربری نمیتواند کمتر از 4 کاراکتر باشد')
#         ]
#         )
#
#     Email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'class':'form-control','placeholder':'hello@example.com'}
#         ),
#         validators=[
#             validators.EmailValidator(message='ایمیل وارد شده صحیح نمیباشد')
#         ]
#         )
#
#     Password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class':'form-control','placeholder':'رمز'}
#         ))
#
#     Confirm_Password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class':'form-control','placeholder':'رمز دوباره'}
#         ))
