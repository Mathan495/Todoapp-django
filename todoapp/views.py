from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos' : all_todos 
    }
    return render(request, 'todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Passwrod too short')
            return redirect('register')

        if username == "":
            messages.error(request, 'Enter your name')
            return redirect('register')
        
        getall_username = User.objects.filter(username=username)
        if getall_username:
            messages.error(request, 'username is already exist')
            return redirect('register')

        # print(username, email, password)
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save() 

        messages.success(request, 'User successfully created, login now')
        return redirect('login') 

    return render(request, 'register.html', {})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass') 

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('homepage') 
        else:
            messages.error(request, 'Error, wrong user details')
            return redirect('login')


    return render(request, 'login.html', {})

@login_required
def Deletetask(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('homepage')

@login_required
def Update(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('homepage')

def logout_view(request):
    logout(request)
    return redirect('login') 