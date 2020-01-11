from django.db import models

# Create your models here.

class Lyrics(models.Model):
    username = models.CharField(max_length=20)
    songname = models.CharField()
    lyrics = models.TextField()