from django.db import models
from network_lab.apps.members.models import Member
from network_lab.apps.projects.models import Topic
# Create your models here.
class Research(models.Model):
    """
    Model for research, a research is an investigation that probably ends with a paper
    """
    # Name of the research
    name = models.TextField(max_length=100)
    # Description of the research
    description = models.TextField()
    # All members who participate in research
    members = models.ManyToManyField(Member)
    # Topics related to Research
    topics = models.ManyToManyField(Topic)
