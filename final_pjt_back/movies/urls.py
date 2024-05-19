from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/add_to_wishlist/', views.add_to_wishlist),
    path('<int:pk>/add_to_watched/', views.add_to_watched),
    path('recommend/', views.fetch_movies_from_tmdb),
    path('recommend/<str:country>/', views.recommend_movies),
    path('recommend/detail/<int:movie_id>/', views.movie_detail),
]