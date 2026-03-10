from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post
from parse_hitmos import EnteredTrack

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'music/index.html', context)

def categories(request, pk):
    return HttpResponse(f'<h1>Категории музыки {pk}</h1>')

def rock(request):
    return render(request, 'music/rock.html')

def all_music(request):
    return render(request, 'music/music.html')


def tracks_rock(request):
    data = EnteredTrack('linkin park', 10).get_all
    return render(request, 'music/rock_tracks.html', context=data)