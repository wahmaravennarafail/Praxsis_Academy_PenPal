from django.db import models


class pesan(models.Model):
    pesan = models.TextField()
    negara = models.CharField(max_length=20)
    initial = models.CharField(max_length=10)
