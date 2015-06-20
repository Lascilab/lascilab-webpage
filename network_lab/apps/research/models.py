from django.db import models

# Create your models here.
class Research(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField()
