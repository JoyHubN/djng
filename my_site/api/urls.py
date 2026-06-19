from django.urls import path

from .views import PostsAPIView

app_name = 'api-v1'

urlpatterns = [
    path('posts/', PostsAPIView.as_view(), name='filter'),
]
