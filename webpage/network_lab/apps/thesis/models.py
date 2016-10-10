from django.db import models
from network_lab.apps.members.models import Member
from network_lab.apps.projects.models import Topic
# Create your models here.
class Thesis(models.Model):
    """
    Model for thesis
    """
    # Name of the thesis
    name = models.TextField(max_length=100)
    # Description of the thesis
    description = models.TextField()
    # Name of the director
    director = models.CharField(max_length=100, blank=True, null=True)
    # Link to the thesis
    link = models.URLField()
    # All members who work on the thesis
    members = models.ManyToManyField(Member)
    # Topics related to the thesis
    topics = models.ManyToManyField(Topic)