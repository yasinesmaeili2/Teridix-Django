from django.urls import path
from .views import (
    AccountView
)


app_name = 'Teridix_account'

urlpatterns = [
    path('account',AccountView,name='account')   
]