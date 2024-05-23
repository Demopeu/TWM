from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    trophys = serializers.CharField(required=False, allow_blank=True)
    like_genres = serializers.DictField(required=False, default={})

    class Meta:
        model = User
        fields = '__all__'
    
    def update(self, instance, validated_data):
        like_genres_data = validated_data.pop('like_genres', None)
        if like_genres_data is not None:
            instance.like_genres = like_genres_data
        return super().update(instance, validated_data)
        

