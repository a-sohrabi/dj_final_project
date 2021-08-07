from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     USERNAME_FIELD = 'phone'
#
#     phone = models.CharField(max_length=15, unique=True)
#     invite_code = models.CharField(max_length=40, blank=True)
#
#
# class Address():
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=20)
#     province = models.CharField(max_length=20)
