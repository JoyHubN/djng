from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Страница приложения music')

def categories(request, pk):
    return HttpResponse(f'<h1>Категории музыки {pk}</h1>')