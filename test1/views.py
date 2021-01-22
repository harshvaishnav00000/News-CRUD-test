from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.models import User
from .models import newcrud

def index(request):
    b = newcrud.objects.all()
    return render(request, 'index.html', {'item' : b})


def add(request):
    return render(request, 'add.html')


def handleadd(request):
    b = newcrud()
    b.title = request.POST['title']
    b.head0 = request.POST['head']
    b.chead0 = request.POST['content']
    b.id = request.user.id
    b.save()

    return redirect('/')


def show(request, id):
    post = newcrud.objects.filter(post_id = id)
    s = int(request.user.id)
    t = int(post[0].id)
    return render(request, 'show.html', {'item' : post, 's': s, 't': t})


def update(request, id):
    post = newcrud.objects.filter(post_id = id)
    s = int(request.user.id)
    t = int(post[0].id)
    return render(request, 'update.html', {'item' : post})

def handleupdate(request, id):
    b = newcrud.objects.filter(post_id = id)[0]
    b.title = request.POST['title']
    b.head0 = request.POST['head']
    b.chead0 = request.POST['content']
    # b.id = request.user.id
    b.save()

    return redirect('/')

def delete(request, id):
    b = newcrud.objects.filter(post_id = id)[0]
    b.delete()
    return redirect('/')



def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def handlelogin(request):
    email=request.POST['email']
    password=request.POST['password']
    user=authenticate(username= email, password= password)
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
