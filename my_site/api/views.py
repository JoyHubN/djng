from django.shortcuts import render
from rest_framework import generics

from .serializer import PostSerializer
from posts.models import Post

# Create your views here.
class PostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer