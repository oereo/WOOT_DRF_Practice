from django.db import models
from rest_framework import mixins

from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from usermanagers import defaultmanager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique= True)
    age = models.CharField(max_length = 10, unique = False)
    nickname = models.CharField(max_length = 15, unique = True)
    email = models.EmailField(blank = True)
    birth_date = models.DateField()
    is_staff = models.BooleanField(default = False)

