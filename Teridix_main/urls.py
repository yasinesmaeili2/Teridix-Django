from django.urls import path
from .views import (
    BlogView,
    BlogSingleView
)

app_name = 'Teridix_main'

urlpatterns = [
    path('',BlogView,name='blog'),
    path('blog-single/<slug:slug>/<int:pk>/',BlogSingleView,name='blog-single')
]