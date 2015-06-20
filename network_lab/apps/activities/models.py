from django.db import models

# Create your models here.
class Activity(models.Model):
    place = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    encharged = models.CharField(max_length=100)
