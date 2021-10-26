from django.urls import path, include
from . views import *


urlpatterns = [
    path('', home, name="home"),
    path('login', login, name='login'),
    path('detail/<id>', detail, name='detail'),
    path('hapus/<id>', hapus, name='hapus'),
]
