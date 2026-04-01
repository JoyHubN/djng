from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('categories/<str:genre>/', views.categories, name='categories'),
    path('rock/tracks/', views.tracks_rock, name='rock_tracks'),
    path('rock/', views.rock, name='rock'),
]

handler404 = views.page_not_found



