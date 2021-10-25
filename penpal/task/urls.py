from django.urls import path, include
from . views import *
from penpal.task import views
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name='login'),
    path('pesan', pesan, name='pesan'),
    path('profile/', views.profile),


]
