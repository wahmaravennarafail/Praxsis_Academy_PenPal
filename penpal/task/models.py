from django.db import models
from django.db.models.base import Model
from django.utils import timezone


class message(models.Model):
    pesan = models.TextField()
    negara = models.CharField(max_length=20)
    initial = models.CharField(max_length=10)


class login(models.Model):
    email = models.CharField(max_length=20)
    password = models.IntegerField()


<<<<<<< HEAD
=======
class profilPost(models.Model):
    posting = models.CharField(max_length=200)


>>>>>>> 9f7d8dbb89207b8968e6b437794b3eeaf9b1416a
# class userProfile(models.Model):
#     user = models.OneToOneField(User, primary_key=True, verbose_name='user',
#                                 related_name='profile', on_delete=models.CASCADE)
#     name = models.CharField(max_length=30, blank=True, null=True)
#     bio = models.TextField(max_length=500, blank=True, null=True)
#     birth_date = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
