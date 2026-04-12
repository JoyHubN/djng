from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProfileUserForm, ResetUserForm

@login_required
def profile(request):
    if request.method == 'POST':
        if 'first_name' in request.POST or 'last_name' in request.POST:
            user_form = ProfileUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                if user_form.changed_data:
                    user_form.save()
                    messages.success(request, 'Профиль успешно обновлён!')
                    return redirect('profile:main')
                else:
                    if 'old_password' in request.POST and 'new_password1' in request.POST and 'new_password2' in request.POST:
                        password_form = ResetUserForm(user=request.user, data=request.POST)
                        if password_form.is_valid():
                            user = password_form.save()
                            update_session_auth_hash(request, user)
                            messages.success(request, 'Пароль успешно изменён!')
                            return redirect('profile:main')
                        else:
                            messages.error(request, 'Ошибка при смене пароля')
        
        else:
            if 'old_password' in request.POST and 'new_password1' in request.POST and 'new_password2' in request.POST:
                password_form = ResetUserForm(user=request.user, data=request.POST)
                if password_form.is_valid():
                    user = password_form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Пароль успешно изменён!')
                    return redirect('profile:main')
                else:
                    messages.error(request, 'Ошибка при смене пароля')
            else:
                messages.error(request, 'Ошибка при смене пароля')
    else:
        user_form = ProfileUserForm(instance=request.user)
        password_form = ResetUserForm(user=request.user)

    context = {
        'form': user_form,
        'password_form': password_form,
    }

    return render(request, 'profil/profil.html', context)