from django import forms



class SinginForm(forms.Form):
    UserName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خودرا وارد کنید...'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز خودرا وارد کنید...'}))