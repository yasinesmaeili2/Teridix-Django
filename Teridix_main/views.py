from django.shortcuts import render
from .models import (
    Blog,
    Category
)


def BlogView(request):
    category = Category.objects.all()

    c = {
        'category':category
    }

    return render(request,'Views/blog.html',c)


def BlogSingleView(requeset,slug,pk):
    blog = Blog.objects.filter(status='T').order_by('create')

    c = {
        'posts':blog
    }

    return render(requeset,'Views/blog-single.html',c)


        