from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True)

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey('bookshelf.Library', on_delete=models.CASCADE)
