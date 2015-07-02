from django.db import models

# Create your models here.
class Member(models.Model):
    """
    Moel for a member, a memper is the public profile for a member of lascilab
    """
    # Name of the member
    name = models.TextField(max_length=100)
    # Email of the member
    email = models.EmailField()
    # Github URL of the member
    github_url = models.URLField()
    # Self description of the member
    description = models.TextField()
    # Set of interest of the member
    interest = models.TextField()
