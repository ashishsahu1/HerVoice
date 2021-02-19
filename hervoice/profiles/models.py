from typing import BinaryIO
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="No Bio ...")
    email = models.EmailField(max_length=254, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png',upload_to='')

    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique = True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

    def save(self, *args, **kwargs):
        pass