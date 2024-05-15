from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MovieSerializer(serializers.ModelSerializer):
    wishlist_users = UserSerializer(many=True, read_only=True)
    watched_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class WishlistSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()

class WatchedSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()