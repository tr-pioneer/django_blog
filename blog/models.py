from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='', default="avatar.png", blank = True)