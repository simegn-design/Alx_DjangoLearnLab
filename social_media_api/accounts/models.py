from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    # Fix: Use proper related_name to avoid clashes
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followers_set',  # Changed to avoid clash
        verbose_name='users that this user follows'
    )
    
    def __str__(self):
        return self.username
    
    @property
    def followers_count(self):
        return self.followers_set.count()  # Updated to match related_name
    
    @property
    def following_count(self):
        return self.following.count()
