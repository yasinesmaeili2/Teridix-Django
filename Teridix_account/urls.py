from django.urls import path
from .views import (
    AccountView,
    LoginView,
    LogoutRequest,
    Updating,
    Creating,
    Deleting,
    Profile,
)
from django.contrib.auth.views import PasswordChangeView


app_name = 'Teridix_account'

urlpatterns = [
    path('account',AccountView,name='account'),
    path('account/sign-in/',LoginView,name='login'),
    # path('account/sign-up/',RegisterView,name='register'),
    path('account/sing-out/',LogoutRequest,name='logout'),
    path('account/update-view/<int:pk>/',Updating.as_view(),name='update'),
    path('account/create-view/',Creating.as_view(),name='create'),
    path('account/delete-view/<int:pk>/',Deleting.as_view(),name='delete'),
    path('account/profile-view/',Profile.as_view(),name='profile'),
    path('account/password-change/',PasswordChangeView.as_view(),name='change-password'),
]
