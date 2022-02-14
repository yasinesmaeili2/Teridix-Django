from django.shortcuts import render
from Teridix_main.models import Blog
from django.contrib.auth.decorators import login_required



@login_required
def AccountView(request):

    blog = Blog.objects.all()
    c = {
        'posts':blog
    }
    return render(request,'View/accounts.html',c)