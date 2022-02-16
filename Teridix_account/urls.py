from django.urls import path
from .views import (
    AccountView,
    LoginView
)


app_name = 'Teridix_account'

urlpatterns = [
    path('account',AccountView,name='account'),
    path('account/sign-in/',LoginView,name='login'),   
]