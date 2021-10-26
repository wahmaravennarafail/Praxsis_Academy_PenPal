from django.urls import path, include
from . views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name='login'),
    path('pesan', pesan, name='pesan'),
]
