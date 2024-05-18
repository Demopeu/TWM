from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=20)
    overview = models.TextField()
    rating = models.FloatField()
    country = models.TextField()
    release_date = models.TextField()
    poster_image = models.URLField()
    trailer_video = models.URLField()
    genre = models.TextField()
    certification = models.TextField()

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_watched = models.BooleanField(default=False)