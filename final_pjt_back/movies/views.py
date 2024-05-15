from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import WishlistSerializer, WatchedSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, pk):
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        movie = get_object_or_404(Movie, pk=pk)
        user = request.user

        if movie.wishlist_users.filter(id=user.id).exists():
            return Response({'detail': 'Movie already in wishlist.'}, status=status.HTTP_400_BAD_REQUEST)

        movie.wishlist_users.add(user)
        return Response({'detail': 'Movie added to wishlist.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watched(request, pk):
    serializer = WatchedSerializer(data=request.data)
    if serializer.is_valid():
        movie = get_object_or_404(Movie, pk=pk)
        user = request.user

        if movie.watched_users.filter(id=user.id).exists():
            return Response({'detail': 'Movie already in watched list.'}, status=status.HTTP_400_BAD_REQUEST)

        movie.watched_users.add(user)
        return Response({'detail': 'Movie added to watched list.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)