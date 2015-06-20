from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    github_url = models.URLField()
    description = models.TextField()
    interest = models.TextField()