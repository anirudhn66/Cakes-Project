from django.db import models

from django.shortcuts import render

# Create your models here.

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

  ADMIN = 'Admin','Admin'

  USER = 'User','User'

class Profile(AbstractUser):

  role = models.CharField(max_length=20)

  class Meta:

    verbose_name = 'Profiles'

    verbose_name_plural = 'Profiles'

  def __str__(self):
    
    return self.first_name