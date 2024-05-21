from rest_framework import serializers
from .models import Movie, Wishlist
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user.id', queryset=User.objects.all())
    movie_id = serializers.PrimaryKeyRelatedField(source='movie.id', queryset=Movie.objects.all())
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    movie_poster = serializers.CharField(source='movie.poster_image', read_only=True)

    class Meta:
        model = Wishlist
        fields = ['user_id', 'movie_id', 'is_watched', 'movie_title', 'movie_poster']