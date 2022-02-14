from django import forms


class ContactForm(forms.Form):
    Full_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کامل'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'hello@domain.com'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'به ما بگویید در چه مواردی میتوانیم کمک کنیم!'}))