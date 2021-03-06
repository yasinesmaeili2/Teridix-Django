from django.urls import path
from .views import (
    BlogView,
    BlogSingleView,
    ContactUsView,
    CategoryView,
    SearchView
)

app_name = 'Teridix_main'

urlpatterns = [
    path('',BlogView,name='blog'),
    path('blog-single/<slug:slug>/<int:pk>/',BlogSingleView,name='blog-single'),
    path('contact/',ContactUsView,name='contact'),
    path('blog/<category_slug>/',CategoryView.as_view(),name='category'),
    path('search/',SearchView.as_view(),name='search'),
]
