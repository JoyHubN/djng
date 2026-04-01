from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from parse_hitmos import EnteredTrack

# Create your views here.

def categories(request: WSGIRequest, genre: str):
    return HttpResponse(f'<h1>Категории музыки {genre}</h1><br>Запрос<br>{request.path_info}{dict(request.GET)}')

def rock(request):
    return render(request, 'music/rock.html')

def index(request):
    return render(request, 'music/music.html')

def tracks_rock(request):
    result = EnteredTrack('limp bizkit', 40).get_all
    first_author = result['items'][0]['author']

    data = {
        'items': result['items'],
        'first_author': first_author,
        }


    return render(request, 'music/rock_tracks.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


