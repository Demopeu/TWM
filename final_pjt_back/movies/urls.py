from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/add_to_wishlist/', views.add_to_wishlist),
    path('<int:pk>/add_to_watched/', views.add_to_watched),
]