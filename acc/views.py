from django.shortcuts import render, redirect

from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(req):
    context = {}
    return render(req, 'acc/index.html', context)


def login(req):
    context = {}

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('index')
        else:
            messages.info(req, 'user not found or password is incorrect')
            return redirect('login')
    else:
        return render(req, 'acc/login.html', context)


def register(req):
    context = {}

    if req.method == "POST":
        username = req.POST.get('username')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req, 'username already exists')
                print('user already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                print('registred '+ username)
                return redirect('login')
        else:
            messages.info(req, 'passwords are different')
            print('passwords are different')
            return redirect('register')
    else:
        return render(req, 'acc/register.html', context)


def logout(req):
    auth.logout(req)
    return render(req, 'acc/index.html')