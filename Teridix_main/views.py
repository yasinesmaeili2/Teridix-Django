from django.shortcuts import render
from django.db.models import Count
from .models import (
    Blog,
    Category
)


def BlogView(request):
    blog = Blog.objects.filter(status='T')
    category = Category.objects.all()
    count_post_by_category = Category.objects.all().annotate(blogs_count=Count('blog'))
    # print(count_post_by_category)

    c = {
        'category':category,
        'posts':blog,
        'cc':count_post_by_category
    }

    return render(request,'Views/blog.html',c)


def BlogSingleView(requeset,slug,pk):
    

    return render(requeset,'Views/blog-single.html')


        