from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import AbstractUser
import os



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.id}{ext}'
    return f'profile/{final_name}'



# Custom User
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_auther = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    image = models.ImageField(null=True,blank=True,upload_to=upload_image_path)