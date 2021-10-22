from django.db import models
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def pesan(request):
    if request.POST:
        pesan = request.POST['pesan']
        negara = request.POST['negara']
        initial = request.POST['initial']
        models.pesan.objects.create(
            pesan=pesan, negara=negara, initial=initial)
    data = models.pesan.objects.all()
    return render(request, 'pesan.html', {
        'data': data
    })
