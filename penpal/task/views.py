from django.db import models
from django.shortcuts import render, redirect
from . import models

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


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
