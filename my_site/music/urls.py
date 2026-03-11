from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('music/', views.all_music),
    path('music/categories/<str:genre>/', views.categories, name='categories'),
    path('music/rock/', views.rock),
    path('music/rock/tracks/', views.tracks_rock),
]