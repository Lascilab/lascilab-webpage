from django.db import models

# Create your models here.
class Member(models.Model):
    """
    Moel for a member, a memper is the public profile for a member of lascilab
    """
    # Profile picture
    picture = models.ImageField(upload_to='img',null=True,blank=True)
    # Name of the member
    name = models.TextField(max_length=100)
    # Email of the member
    email = models.EmailField()
    # Github URL of the member
    github_url = models.URLField(null=True,blank=True)
    # google url of the member
    google_url = models.URLField(null=True,blank=True) 
    # Self description of the member
    description = models.TextField()
    # Set of interest of the member
    interest = models.TextField()
