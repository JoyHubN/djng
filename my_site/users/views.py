from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout


# Create your views here.

from .forms import LoginUserForm

def login_user(request):
    # active_sessions = Session.objects.filter(expire_date__gt=timezone.now())
    session_id = request.COOKIES.get('sessionid')
    if session_id:
        session = Session.objects.get(session_key=session_id)
        data = session.get_decoded()
        
        if data:
            return redirect(reverse('music:index'))    

    if request.method ==  'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('music:index'))
            else:
                return render(request, 'users/login.html', {'form': form, 'message': 'Неверный логин или пароль'})

    else:
        form = LoginUserForm()

    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('music:index'))