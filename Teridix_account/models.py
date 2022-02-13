from asyncio import FastChildWatcher
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_auther = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')

    def __str__(self):
        return self.is_auther