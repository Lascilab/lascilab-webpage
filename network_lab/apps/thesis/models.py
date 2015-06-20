from django.db import models

# Create your models here.
class Thesis(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    link = models.URLField()