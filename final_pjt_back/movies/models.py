from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    wishlist_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wishlist_movies')
    watched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watched_movies')
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=20)
    overview = models.TextField()
    rating = models.FloatField()
    country = models.TextField()
    poster_image = models.URLField()
    trailer_video = models.URLField()
    genre = models.TextField()
