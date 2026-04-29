from django.shortcuts import render

# Create your views here.
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Post

def index(request):
    context = {}
    flag_search = False

    index = 'posts/index.html'
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


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def filter(request):
    context = {}
    flag_search = False
    index = 'posts/index.html'

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


def create(request):
    return HttpResponse('<h1>создать статью</h1>')


def delete(request, pk:int):
    return HttpResponse('<h1>удалить статью</h1>')

def edit(request, pk:int):
    return HttpResponse('<h1>редактировать статью</h1>')