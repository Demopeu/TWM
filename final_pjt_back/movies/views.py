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

def get_genre_mapping(api_key):
    genre_mapping = {}
    base_url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'api_key': api_key,
        'language': 'en-US',
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    for genre in data['genres']:
        genre_mapping[genre['id']] = genre['name']
    return genre_mapping

def fetch_movies_from_tmdb(request):
    url = "https://api.themoviedb.org/3/discover/movie"
    api_key = '6a9c6e33e06ff2c5f1ce2c6ff0f950cd'
    genre_mapping = get_genre_mapping(api_key)
    countries = ['US', 'CA', 'MX', 'BR', 'AR', 'CL', 'VE', 'CO', 'GB', 'FR', 'DE', 'IT', 'RU', 'ID', 'CN', 'KR', 'CA']
    for country_name in countries:
        params = {
            'api_key': api_key,
            'page': 1,
            'with_origin_country': country_name,
            'region': 'KR',
            'per_page': 20,
            'sort_by': 'popularity.desc',  # 인기있는 영화 기준으로 정렬
            'include_adult': False,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            for movie_data in movies:
                tmdb_id=movie_data['id']
                title=movie_data['title']
                overview=movie_data['overview']
                rating=movie_data['vote_average']
                country=country_name
                poster_image=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
                trailer_video=''
                if movie_data['video']:
                    trailer_video = f"https://www.youtube.com/watch?v={movie_data['video']}"
                genre_ids = movie_data['genre_ids']
                genres = [genre_mapping.get(genre_id, 'Unknown') for genre_id in genre_ids]
                genre = ', '.join(genres)

                Movie.objects.create(
                    tmdb_id=tmdb_id,
                    title=title,
                    overview=overview,
                    rating=rating,
                    country=country,
                    poster_image=poster_image,
                    trailer_video=trailer_video,
                    genre=genre
                )
    return JsonResponse({'message': 'Movies fetched successfully'})


@api_view(['GET'])
def recommend_movies(request, country):
    if request.method == 'GET':
        if country == 'north_america':
            country = ['US', 'CA', 'MX']
        elif country == 'south_americal':
            country = ['BR', 'AR', 'CL', 'VE']
        elif country == 'europe':
            country = ['GB', 'FR', 'DE', 'IT', 'RU']
        elif country == 'india':
            country = ['ID']
        elif country == 'korea':
            country = ['KR']
        elif country == 'china':
            country = ['CN']
        elif country == 'japan':
            country = ['JP']
        
        result = []
        for cont in country:
            movies = Movie.objects.filter(country=cont)
            result.extend(movies)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
