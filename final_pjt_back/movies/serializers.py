from rest_framework import serializers
from .models import Movie, Wishlist
from django.contrib.auth import get_user_model

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'