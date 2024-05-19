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

    class Meta:
        model = Wishlist
        fields = ['user_id', 'movie_id', 'is_watched']