from django.http import Http404
from django.shortcuts import get_object_or_404
# from Teridix_main.models import Blog


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
            raise Http404('شما نمیتوانید این صفحه را مشاهده کنید!')

        
        return super().dispatch(request,*args,**kwargs)

        