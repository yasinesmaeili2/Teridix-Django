from ast import arg
from django.db import models
from Teridix_account.models import User
from django.urls import reverse
from django.db.models import Q


class Manager(models.Manager):
    def get_post_by_category(self,category_slug):
        return self.get_queryset().filter(categories__category_slug__iexact=category_slug,status='T')


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField(max_length=120)

    def __str__(self):
        return self.category_name


class Blog(models.Model):

    STATUS = (
        ('T','True'),
        ('F','False'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='BlogImage')
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    create = models.DateField(auto_created=True,auto_now_add=True)
    status = models.CharField(max_length=1,default='F',choices=STATUS)
    objects = Manager()


    def __str__(self):
        return self.title

    def get_absolute_url_blog_single(self):
        return reverse('Teridix_main:blog-single',args=[self.slug,self.id])

    