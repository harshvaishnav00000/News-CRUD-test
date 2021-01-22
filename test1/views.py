from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.models import User
from .models import Blogpost


def index(request):
    b = Blogpost.objects.all()
    return render(request, 'index.html', {'item' : b})


def add(request):
    return render(request, 'add.html')


def handleadd(request):
    b = Blogpost()
    b.title = request.POST['title']
    b.head0 = request.POST['head']
    b.chead0 = request.POST['content']
    b.save()

    return redirect('/')


def show(request, id):
    post = Blogpost.objects.filter(post_id = id)
    return render(request, 'show.html', {'item' : post})



def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def handlelogin(request):
    email=request.POST['email']
    password=request.POST['password']
    user=authenticate(username= email, password= password)
    print(user)
    if user is not None:
        Login(request, user)
        return redirect("/")
    else:
        return redirect("/")


def logout(request):
    Logout(request)
    return redirect('/')

def handlesignup(request):

    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    username = email
    if password1 != password2:
        return render(request, 'Signup.html')

    myuser = User.objects.create_user(username, email, password1)
    myuser.save()
    return redirect('/')
