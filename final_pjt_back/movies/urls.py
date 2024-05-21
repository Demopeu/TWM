from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/add_to_wishlist/', views.add_to_wishlist),
    path('<int:pk>/add_to_watched/', views.add_to_watched),
    path('<int:user_id>/get_wishlist/', views.get_wishlist),
    # 임시로 영화데이터 받아오는 경로(movies/recommend/ 입력하면 됨!)
    path('recommend/', views.fetch_movies_from_tmdb),
    path('recommend/<str:country>/', views.recommend_movies),
    path('recommend/detail/<int:movie_id>/', views.movie_detail),
]