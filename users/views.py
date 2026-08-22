from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_mail(
                'Добро пожаловать!',
                'Вы успешно зарегистрировались на нашем сайте.',
                'noreply@myshop.ru',
                [user.email],
                fail_silently=True,
            )
            messages.success(request, 'Регистрация успешна!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы вошли!')
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли.')
    return redirect('index')
