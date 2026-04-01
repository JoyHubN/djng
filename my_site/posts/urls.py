from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.filter, name='filter'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
]
