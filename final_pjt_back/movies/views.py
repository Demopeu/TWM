from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Wishlist
from .serializers import WishlistSerializer, MovieSerializer
import requests
from django.http import JsonResponse


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user
    
    if Wishlist.objects.filter(movie=movie, user=user).exists():
        return Response({'detail': 'Movie already in wishlist.'}, status=status.HTTP_400_BAD_REQUEST)
    
    data = {'movie': movie.pk, 'user': user.pk}
    serializer = WishlistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Movie added to wishlist.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watched(request):
    movie_id = request.data.get('movie_id')
    user_id = request.data.get('user_id')

    wishlist_items = Wishlist.objects.filter(user_id=user_id, movie_id=movie_id)

    if wishlist_items.exists():
        wishlist_item = wishlist_items.first()
        wishlist_item.is_watched = True
        wishlist_item.save()

        serializer = WishlistSerializer(wishlist_item)

        return Response(serializer.data)
    else:
        return Response({'error': 'Movie not found in wishlist'}, status=status.HTTP_404_NOT_FOUND)

def fetch_movies_from_tmdb(request):
    url = "https://api.themoviedb.org/3/discover/movie"
    api_key = '6a9c6e33e06ff2c5f1ce2c6ff0f950cd'
    countries = ['US', 'CA', 'MX', 'BR', 'AR', 'CL', 'VE', 'CO', 'GB', 'FR', 'DE', 'IT', 'RU', 'ID', 'CN', 'KR', 'JP']
    for country in countries:
        params = {
            'api_key': api_key,
            'with_original_language': country,
            'page': 1,
            'per_page': 300,
            'sort_by': 'vote_average.desc'  # 인기있는 영화 기준으로 정렬
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()['results']
            for movie_data in data:
                trailer_url = get_trailer_video_url(movie_data['id'], api_key)

                movie = Movie(
                    tmdb_id=movie_data['id'],
                    title=movie_data['title'],
                    overview=movie_data['overview'],
                    rating=movie_data['vote_average'],
                    country=country.upper(),  
                    poster_image=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
                    trailer_video=trailer_url,  
                    genre=','.join([genre['name'] for genre in movie_data['genres']])  
                )
                movie.save()  

    return JsonResponse({'message': 'Movies fetched successfully'})

def get_trailer_video_url(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['results']
        for video_data in data:
            if video_data['type'] == 'Trailer' and video_data['official']:
                youtube_video_id = video_data['key']
                return f"https://www.youtube.com/watch?v={youtube_video_id}"

    return ''



