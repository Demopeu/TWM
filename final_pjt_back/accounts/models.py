from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    trophys = models.TextField(blank=True, null=True)
    like_genres = models.JSONField(default=dict)
