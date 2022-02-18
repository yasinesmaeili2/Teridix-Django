from django.http import Http404
from django.shortcuts import get_object_or_404
from Teridix_main.models import Blog


# show fields for superuser and just author
# and add class name in views.py class ArticelCreate.
class FieldMixin():

    def dispatch(self,request,*args,**kwargs):
        # show all fields for superuser
        if request.user.is_superuser:
            self.fields = [
                'title',
                'slug',
                'image',
                'description',
                'categories',
                'author',
                'status'
            ]

        # show field for author
        elif request.user.is_auther:
            self.fields = [
                'title',
                'slug',
                'image',
                'description',
                'categories',
            ]
        else:
            raise Http404('شما نمیتوانید این صفحه را مشاهده کنید! FieldMixin')

        
        return super().dispatch(request,*args,**kwargs)

        

# for CreateView Form
class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()

        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'F'
        return super().form_valid(form)



# show post for just auhotor and superuser 
class AccessBlogMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        blog = get_object_or_404(Blog,pk=pk)
        if blog.author == request.user and blog.status == 'F' or request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404('شما نمیتوانید این صفحه را مشاهده کنید AccessBlog !')


# for Deleting post -> just superuser
class SuperuserAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما نمیتوانید این صفحه را مشاهده کنید! SuperUser')