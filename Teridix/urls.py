"""Teridix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Teridix_main.urls')),
    path('',include('Teridix_account.urls')),

    # 1
    path('password-reset/',PasswordResetView.as_view(),name='PRE'),
    
    # 2
    path('password-reset/done', PasswordResetDoneView.as_view(),name='password_reset_done'),

    # 3
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    # 4
    path('password-done/',PasswordResetCompleteView.as_view(),name='password_reset_complete')
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)