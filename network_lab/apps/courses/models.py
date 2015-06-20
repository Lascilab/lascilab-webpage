from django.db import models

# Create your models here.
class Course(models.Model):
    place = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    horary = models.TextField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=100)
    encharged = models.CharField(max_length=100)