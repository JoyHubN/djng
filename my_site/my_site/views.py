from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import generics

from .models import Post
from parse_hitmos import EnteredTrack

# Create your views here.

def index(request):
    context = {}
    flag_search = False

    index = 'music/index.html'
    context['title'] = 'Главная страница'

    if request.GET:
        context['title'] = 'Поиск по тексту'
        q = request.GET.get('q')
        if q:
            flag_search = True
            result = Post.objects.filter(text__contains = q)
            
            context['quest'] = q
            context['posts'] = result
        else:    
            posts = Post.objects.order_by('-pub_date')[:10]
            context['posts'] = posts
    
    elif request.path == '/':
        posts = Post.objects.order_by('-pub_date')[:10]
        context['posts'] = posts

    context['search'] = flag_search
    return render(request, index, context)


def categories(request: WSGIRequest, genre: str):
    req = dict(request) if request else None  
    return HttpResponse(f'<h1>Категории музыки {genre}</h1><br>Запрос<br>{request.path_info}{dict(request.GET)}')

def rock(request):
    return render(request, 'music/rock.html')

def all_music(request):
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


def posts(request):
    context = {}
    flag_search = False
    index = 'music/index.html'

    get_data = request.GET

    if get_data.get('filter'):
        if get_data['filter'] == 'author':
            if get_data.get('q'):
                quest = get_data['q'].split(' ')

                query = Q()

                for part in quest:
                    query &= (
                        Q(author__first_name__icontains=part) | 
                        Q(author__last_name__icontains=part)
                    ) 

                posts_result = Post.objects.filter(query)
                
                if posts_result:
                    flag_search = True
                    context['filter'] = get_data['filter']
                    context['quest'] = ' '.join(quest)
                    context['posts'] = posts_result
                    

    
    context['title'] = 'Поиск по автору'
    context['search'] = flag_search
                
    return render(request, index, context)


