from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.views.generic import ListView
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



class CategoryView(ListView):
    template_name = 'Views/blog.html'
    context_object_name = 'posts'


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cc'] = Category.objects.all().annotate(blogs_count=Count('blog'))
        context['bOrder'] = Blog.objects.filter(status='T').order_by('-create')
        return context        
    
    def get_queryset(self):

        category_slug = self.kwargs['category_slug']
        category = Category.objects.filter(category_name__iexact=category_slug).first()
        if category is None:
            pass
        return Blog.objects.get_post_by_category(category_slug)