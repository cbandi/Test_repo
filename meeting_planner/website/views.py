from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect

from meetings.models import Meeting


def welcome(response):
    return render(response, 'website1/welcome.html',
                  {'meetings': Meeting.objects.all()})


def date(response):
    return HttpResponse("current Date is " + str(datetime.now()))


def about(response):
    return HttpResponse("about me")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Unauthorised')
        else:
            return redirect('home')
    return render(request, 'website1/login.html')


def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        email = req.POST['email']
        created = User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user in None:
            return HttpResponse("User registration failed")
        else:
            login(user)
            return HttpResponse("User registration success")
    return render(req, 'website1/register.html')


def user_name(request):
    return HttpResponse("username: "+request.user.username)


def logout_user(request):
    logout(request)
    return HttpResponse("User logged out successfully")


def page_not_found(response):
    return render(response, 'website1/pageNotFound.html')
