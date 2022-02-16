from django.urls import path
from .views import (
    AccountView,
    LoginView,
    LogoutRequest
)


app_name = 'Teridix_account'

urlpatterns = [
    path('account',AccountView,name='account'),
    path('account/sign-in/',LoginView,name='login'),
    path('account/sing-out/',LogoutRequest,name='logout')   
]