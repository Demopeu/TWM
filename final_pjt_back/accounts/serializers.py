from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    trophys = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = '__all__'
        

