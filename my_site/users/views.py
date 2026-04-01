from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout


# Create your views here.

from .forms import LoginUserForm, RegisterUserForm

def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('main:index')  

    if request.method ==  'POST':
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
            else:
                return render(request, 
                              'users/login.html', 
                              {
                                  'form': form, 
                                  'message': 'Неверный логин или пароль'
                                }
                        )

    else:
        form = LoginUserForm()

    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def registration(request):
    
    if request.user.is_authenticated:
        return redirect('main:index')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'users/register_done.html')
    else:        
        form = RegisterUserForm()
    return render(request, 'users/registration.html', {'form': form})