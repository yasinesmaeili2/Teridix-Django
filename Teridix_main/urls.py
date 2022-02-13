from django.urls import path
from .views import Blog

app_name = 'Teridix_main'

urlpatterns = [
    path('',Blog,name='blog')
]