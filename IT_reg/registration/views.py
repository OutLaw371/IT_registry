from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(username, password=password)
                user.save()
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'register.html', {'error': 'Это имя пользователя уже занято'})
        else:
            return render(request, 'register.html', {'error': 'Пароли не совпадают'})
    else:
        return render(request, 'register.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    else:
        return render(request, 'login.html')
