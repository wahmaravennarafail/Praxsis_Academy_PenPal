from django.urls import path, include
from . views import *
<<<<<<< HEAD
from penpal.task import views
=======
>>>>>>> b2b2b69799c270f62cb4279854fc0067efaa9f8c

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name='login'),
    path('pesan', pesan, name='pesan'),
<<<<<<< HEAD



=======
>>>>>>> b2b2b69799c270f62cb4279854fc0067efaa9f8c
]
