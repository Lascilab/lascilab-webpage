from django.db import models
from network_lab.apps.members.models import Member
# Create your models here.
class Event(models.Model):
    """
    An activity is sleep, and I don't like to document at midnigth
    """
    # Place where the activity will live
    place = models.CharField(max_length=200)
    # Creation date of the activity
    creation_date = models.DateTimeField(auto_now=True)
    # Date of the activity
    date = models.DateField()
    # Time of the activity
    time = models.TimeField()
    # Description of the activity
    description = models.TextField()
    # Title of the activity
    title = models.CharField(max_length=100)
    # Encharged of the activity
    encharged = models.ForeignKey(Member, blank=True, null=True)
