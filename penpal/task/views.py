from typing import ContextManager
from django.db import models
from django.shortcuts import render, redirect
from . import models

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def pesan(request):
    if request.POST:
        message = request.POST['message']
        negara = request.POST['negara']
        initial = request.POST['initial']
        models.message.objects.create(
            message=message, negara=negara, initial=initial
        )
    data = models.message.objects.all()
    return render(request, 'home.html', {
        'data': data
    })

def profile(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        models.profile.objects.create(
            username=username, email=email
        )
    data = models.profile.objects.all()
    return render(request, 'home.html', {
        'data': data
    })

# def user(request):
#     if request.POST:

def view_profile(request):
    Context = {
        'user' : request.user
    }
    return render(request,'profile.html', Context )