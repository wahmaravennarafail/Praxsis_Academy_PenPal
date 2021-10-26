from typing import ContextManager
from django.db import models
from django.shortcuts import render, redirect
from . import models


def login(request):
    if request.POST:
        input_email = request.POST['email']
        input_password = request.POST['password']

        user = models.login.objects.filter(email=input_email, password=input_password).first()
        # print(user)
        if user is not None :
        
            return redirect('/profile')
    return render(request, 'task/login.html')

def home(request):
    if request.POST:
        message = request.POST['message']
        negara = request.POST['negara']
        initial = request.POST['initial']
        models.message.objects.create(
            pesan=message, negara=negara, initial=initial)
    data = models.message.objects.all()
    # print("data")
    return render(request, 'task/home.html', {
        'data': data
    })


def detail(request, id):
    data = models.message.objects.filter(pk=id).first()
    print(data)
    return render(request, 'task/detail.html', {
        'detail_pesan': data
    })


def hapus(request, id):
    models.message.objects.filter(pk=id).delete()
    return redirect('/')

def profil (request):
    return render(request, 'task/profile.html')