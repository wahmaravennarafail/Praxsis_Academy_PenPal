from django.urls import path, include
from . views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name='login'),
    path('pesan', pesan, name='pesan'),
    path('profile', view_profile, name='profile'),
]
