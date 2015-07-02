from django.db import models
from network_lab.apps.members.models import Member
# Create your models here.
class Topic(models.Model):
    """
    Model for topics, a topic is a category of interest in lascilab
    """
    # Slugify name for topic
    slug = models.SlugField()
    # Full topic's name
    name = models.TextField(max_length=100)
    # Description of the topic
    description = models.TextField()


class Project(models.Model):
    """
    Model for a project, a project is a set of activities which pretends prove/develop something
    """
    # Name of the project
    name = models.TextField(max_length=100)
    # Members in the projects
    members = models.ManyToManyField(Member)
    # Project's Topics
    topics = models.ManyToManyField(Topic)
    # Description of the projects
    description = models.TextField()
    # Start date of the project
    initial_date = models.DateField()
    # culmination date of the project
    final_date = models.DateField()
    # State of the project: Finished, Active, In process, Non Active
    state = models.CharField(max_length=100, blank=True, null=True)


