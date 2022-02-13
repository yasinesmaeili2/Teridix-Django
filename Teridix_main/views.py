from django.shortcuts import render



def Blog(request):
    return render(request,'Views/blog.html')
