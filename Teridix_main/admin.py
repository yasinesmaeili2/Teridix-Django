from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Blog,
    Category,
    ContactUsModel
)


@admin.action(description='تنظیم وضعیت به حالت False')
def ChangeToFalse(Blog,request,queryset):
    return queryset.update(status='F')

@admin.action(description='تنشظیم وضعیت به حالت True')
def ChangeToTrue(Blog,request,queryset):
    return queryset.update(status='T')


admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    def image_format(self,obj):
        return format_html('<img width=50 src={}/>'.format(obj.image.url))
    
    list_display = ['title','author','create','status','image_format']
    list_filter = ['title','author','status']
    list_search = ['title','description','author']
    prepopulated_fields = {
        'slug':('title',)
    }

    actions = [ChangeToFalse,ChangeToTrue]


@admin.register(ContactUsModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','status']
    list_filter = ['email','status']
    