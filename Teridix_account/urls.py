from django.urls import path
from .views import (
    AccountView,
    LoginView,
    LogoutRequest,
    RegisterView,
    Updating,
    Creating
)


app_name = 'Teridix_account'

urlpatterns = [
    path('account',AccountView,name='account'),
    path('account/sign-in/',LoginView,name='login'),
    path('account/sign-up/',RegisterView,name='register'),
    path('account/sing-out/',LogoutRequest,name='logout'),
    path('account/update-view/<int:pk>/',Updating.as_view(),name='update'),
    path('account/create-view/',Creating.as_view(),name='create')
]