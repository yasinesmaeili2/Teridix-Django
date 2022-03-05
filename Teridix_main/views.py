from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import (
    Blog,
    Category,
    ContactUsModel
)



def BlogView(request):
    blog = Blog.objects.filter(status='T')
    paginator = Paginator(blog, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    blog_order = Blog.objects.filter(status='T').order_by('-create')
    category = Category.objects.all()
    
    # count post by category
    # 'blog' -> class name in models.py file.
    count_post_by_category = Category.objects.all().annotate(blogs_count=Count('blog'))
    c = {
        'category':category,
        'posts':page_obj,
        'cc':count_post_by_category,
        'bOrder':blog_order
    }

    return render(request,'Views/blog.html',c)



def BlogSingleView(requeset,slug,pk):
    blog = get_object_or_404(Blog,slug=slug,id=pk,status='T')
    blog_order = Blog.objects.filter(status='T').order_by('-create')

    # related posts
    related_post = Blog.objects.get_queryset().filter(categories__blog=blog).distinct()[:3]
    
    # count post by category
    count_post_by_category = Category.objects.all().annotate(blogs_count=Count('blog'))
    c = {
        'post':blog,
        'cc':count_post_by_category,
        'bOrder':blog_order,
        'related_post':related_post
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



class SearchView(ListView):
    template_name = 'Views/blog.html'
    context_object_name = 'posts'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cc'] = Category.objects.all().annotate(blogs_count=Count('blog'))
        context['bOrder'] = Blog.objects.filter(status='T').order_by('-create')
        return context 
    
    def get_queryset(self):
        request = self.request
        query = request.GET.get('query')
        if query is not None:
            return Blog.objects.get_post_by_search(query)
        return Blog.objects.filter(status='T')



def ContactUsView(request):
    form = ContactForm(request.POST or None)
    c = {
        'form':form
    }
    if form.is_valid():
        f_name = form.cleaned_data.get('Full_name')
        e = form.cleaned_data.get('Email')
        m = form.cleaned_data.get('Message')
        cm = ContactUsModel.objects.create(full_name=f_name,email=e,message=m)
        cm.save()
        return redirect('Teridix_main:blog')

    return render(request,'Views/contact.html',c)
    