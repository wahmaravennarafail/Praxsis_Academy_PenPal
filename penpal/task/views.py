from django.db import models
from django.shortcuts import render, redirect
from . import models

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.POST:
        input_email = request.POST['email']
        input_password = request.POST['password']

        user = models.login.objects.filter(email=input_email, password=input_password).first()
        # print(user)
        if user is not None :
        
            return redirect('/profil')
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
def profil (request):
    return render(request, 'profile.html')