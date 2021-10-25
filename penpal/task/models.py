from django.db import models
from django.db.models.base import Model


class message(models.Model):
    pesan = models.TextField()
    negara = models.CharField(max_length=20)
    initial = models.CharField(max_length=10)

class login(models.Model):
    email= models.CharField(max_length=20)
    password = models.CharField(max_length=8)
# Create your models here.
