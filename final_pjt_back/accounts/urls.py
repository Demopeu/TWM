from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/', views.get_user_info),
    path('user/<int:user_pk>/', views.signout),
]