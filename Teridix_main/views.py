from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import (
    Blog,
    Category
)


def BlogView(request):
    blog = Blog.objects.filter(status='T')
    blog_order = Blog.objects.filter(status='T').order_by('-create')
    category = Category.objects.all()
    
    #ls count post by category
    count_post_by_category = Category.objects.all().annotate(blogs_count=Count('blog'))


    c = {
        'category':category,
        'posts':blog,
        'cc':count_post_by_category,
        'bOrder':blog_order
    }

    return render(request,'Views/blog.html',c)


def BlogSingleView(requeset,slug,pk):
    
    blog = get_object_or_404(Blog,slug=slug,id=pk)
    blog_order = Blog.objects.filter(status='T').order_by('-create')
    
    # count post by category
    count_post_by_category = Category.objects.all().annotate(blogs_count=Count('blog'))

    c = {
        'post':blog,
        'cc':count_post_by_category,
        'bOrder':blog_order
    }
    

    return render(requeset,'Views/blog-single.html',c)


        