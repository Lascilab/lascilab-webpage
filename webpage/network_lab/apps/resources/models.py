from django.db import models

# Create your models here.
class Resource(models.Model):
    """
    Model for resources, a resource could be anithing that lascilab can offer to community
    """
    # Name of the resource
    name = models.TextField(max_length=100)
    # Description of the resource
    description = models.TextField()