from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.all_music, name='all_music'),
    path('music/categories/<str:genre>/', views.categories, name='categories'),
    path('music/rock/', views.rock, name='rock'),
    path('music/rock/tracks/', views.tracks_rock, name='rock_tracks'),
]

handler404 = views.page_not_found