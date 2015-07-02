from django.db import models
from network_lab.apps.members.models import Member
# Create your models here.
class Course(models.Model):
    """
    Model for a course, a course is a course
    """
    # Location of the course
    place = models.CharField(max_length=200)
    # Creation date of the course
    creation_date = models.DateTimeField(auto_now=True)
    # Schedule of the course
    horary = models.TextField(max_length=200)
    # Description of the course
    description = models.TextField()
    # Title of the course
    title = models.CharField(max_length=100)
    # Responsible for the course
    teacher = models.ForeignKey(Member, blank=True, null=True)
    # Start date of the course
    initial_date = models.DateField(blank=True, null=True)
    # Date of end of the course
    final_date = models.DateField(blank=True, null=True)


class CourseMaterial(models.Model):
    """
    Model for material for the course, a material is all resources tan can be used in the course
    """
    # Reference to the course
    course = models.ForeignKey(Course)
    # Title of the material
    title = models.CharField(max_length=100)
    # Description of the material
    description = models.TextField()
    # URL to get the material
    url = models.URLField()
    # Type of material: PDF, Video, Source code, Link
    type = models.CharField(max_length=20)
