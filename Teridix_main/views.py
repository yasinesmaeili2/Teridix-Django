from django.shortcuts import render



def BlogView(request):
    return render(request,'Views/blog.html')


def BlogSingleView(requeset,slug,pk):

    return render(requeset,'Views/blog-single.html')


        