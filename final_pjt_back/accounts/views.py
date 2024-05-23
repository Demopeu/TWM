from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@api_view(['GET'])
def get_user_info(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def signout(request, user_pk):
    user = User.objects.get(pk=user_pk)

    if not user:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    user.delete()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)