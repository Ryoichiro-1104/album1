import datetime
from django.db import models



# Create your models here.

class List(models.Model):
    singer = models.CharField(max_length=100)
    title = models.CharField (max_length=200)
    time = models.IntegerField()
    lyrics = models.TextField()
    type = models.CharField(max_length=200)
    release_date = models.DateField()

    def table(self):
        self.save()

    def _str_(self):
        return self.title