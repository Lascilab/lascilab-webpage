from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.TextField(max_length=100)
    owner = models.TextField(max_length=100)
    description = models.TextField()
    initial_date = models.DateField()
    final_date = models.DateField()