from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Wishlist
from .serializers import WishlistSerializer, MovieSerializer
import requests
from django.http import JsonResponse
import time
from urllib.parse import quote


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
        'language': 'ko-KR',
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    for genre in data['genres']:
        genre_mapping[genre['id']] = genre['name']
    return genre_mapping


def get_movie_certification(api_key, movie_id):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates"
    params = {
        'api_key': api_key,
    }
    adult = ['19', '19+', '18', '청소년 관람불가', '청소년 관람 불가']
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        for result in data.get('results', []):
            if result.get('iso_3166_1') == 'KR':  # 한국 기준!
                for release in result.get('release_dates', []):
                    if 'certification' in release:
                        certification = release['certification']
                        if certification in adult:  # 성인 영화 제외
                            return None
                        return certification
    return None

# 유튜브 API 요청 코드(임시로 주석처리)
# def get_movie_trailer(title):
#     base_url = "https://www.googleapis.com/youtube/v3/search"
#     api_key = settings.YOUTUBE_API_KEY
#     params = {
#         'q': f"{title} official trailer",
#         'key': api_key,
#         'type': 'video',
#         'part': 'snippet',
#         'maxResults': 1
#     }
#     response = requests.get(base_url, params=params)
#     print(response)
#     if response.status_code == 200:
#         data = response.json()
#         # 검색 결과가 존재하는지 확인
#         if 'items' in data and data["items"]:
#             video_id = data['items'][0]['id']['videoId']
#             return f"https://www.youtube.com/watch?v={video_id}"
    
#     # 검색 결과가 없는 경우 빈값 반환
#     return ""


def fetch_movies_from_tmdb(request):
    url = "https://api.themoviedb.org/3/discover/movie"
    api_key = settings.TMDB_API_KEY
    genre_mapping = get_genre_mapping(api_key)
    countries = ['US'] # ['US', 'CA', 'MX', 'BR', 'AR', 'CL', 'VE', 'CO', 'GB', 'FR', 'DE', 'IT', 'RU', 'ID', 'KR', 'CN', 'JP']
    
    # 초당 요청 수를 제한하기 위한 변수
    requests_per_second = 35
    time_between_requests = 1 / requests_per_second

    for country_name in countries:
        current_page = 1
        while current_page < 2:
            params = {
                'api_key': api_key,
                'page': current_page,
                'with_origin_country': country_name,
                'per_page': 20,
                'language': 'ko-KR'
            }

            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                movies = data['results']
                for movie_data in movies:
                    if not movie_data.get('adult', False) and 'title' in movie_data and 'overview' in movie_data and movie_data['overview']:
                        tmdb_id=movie_data['id']
                        title=movie_data['title']
                        overview=movie_data['overview']
                        rating=movie_data['vote_average']
                        release_date = movie_data['release_date']
                        country=country_name
                        poster_image=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
                        genre_ids = movie_data['genre_ids']
                        genres = [genre_mapping.get(genre_id, 'Unknown') for genre_id in genre_ids]
                        genre = ', '.join(genres)

                        certification = get_movie_certification(api_key, tmdb_id)
                        trailer_video = ''
                        if certification:
                            Movie.objects.create(
                                tmdb_id=tmdb_id,
                                title=title,
                                overview=overview,
                                rating=rating,
                                release_date=release_date,
                                country=country,
                                poster_image=poster_image,
                                trailer_video=trailer_video,
                                genre=genre,
                                certification=certification
                            )
                # 대기 시간 추가
                time.sleep(time_between_requests)

            current_page += 1


    return JsonResponse({'message': 'Movies fetched successfully'})


@api_view(['GET'])
def recommend_movies(request, country):
    if request.method == 'GET':
        if country == 'north_america':
            country = ['US', 'CA', 'MX']
        elif country == 'south_america':
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
        serializer = MovieSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)