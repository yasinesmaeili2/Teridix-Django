from pyexpat import model
from this import d
from django.db import models
from Teridix_account.models import User



class Manager(models.Manager):
    pass


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
    create = models.DateField(auto_created=True)
    status = models.CharField(max_length=1,default='F',choices=STATUS)
    objects = Manager()


    def __str__(self):
        return self.title

    