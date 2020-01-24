from django.db import models

# Create your models here.

class Music(models.Model):
    Username = models.CharField(max_length=20)
    Song_Name = models.CharField(max_length=50)
    Feedback = models.TextField()

    def __str__(self):
        return self.Username + ' ' + self.Song_Name + ' ' + self.Feedback 
