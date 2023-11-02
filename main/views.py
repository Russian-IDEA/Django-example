from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Task


@login_required(login_url='/login')
def home(request):
    tasks = list(request.user.task_set.all())[::-1]
    return render(request, 'index.html', {'user': request.user, 'tasks': tasks})


@login_required(login_url='/login')
def add(request):
    return render(request, 'add.html')


@login_required(login_url='/login')
def post(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Task.objects.create(user=request.user, name=name, description=description)
    return redirect('/')


def login_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        error = 'Пользователь не найден'
    return render(request, 'login.html', {'error': error})


def signup_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            error = 'Пользователь уже существует'
        except Exception:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'signup.html', {'error': error})


def logout_page(request):
    logout(request)
    return redirect('/login')
