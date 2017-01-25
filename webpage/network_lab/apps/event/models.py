from django.db import models
from network_lab.apps.members.models import Member
from django.utils.translation import ugettext_lazy as _

class Topics(models.Model):
    name = models.CharField(_('Event Topic'),max_length=400)

class EventImage(models.Model):
    image = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)

class Event(models.Model):
    """
    An event is sleep, and I don't like to document at midnigth
    """
    # Event banner or picture
    banner = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)
    # Important notes about the event
    important_notes = models.TextField(_('Important Notes'),null=True,blank=True)
    # Important dates about the event
    application_opening = models.DateField(_('Application Opening'),null=True,blank=True)
    application_deadline = models.DateField(_('Application Deadline'),null=True,blank=True)
    admission_notification = models.DateField(_('Admission Notification'),null=True,blank=True)
    registration_deadline = models.DateField(_('Registration Deadline'),null=True,blank=True)
    # The Objective of the event
    mision = models.TextField(_('Event Mision'),null=True,blank=True)
    # Description of the activity
    topics = models.ManyToManyField('Topics')
    # how the activity is going to be organized
    organization = models.CharField(_('Event Organization'),max_length=100,null=True,blank=True)
    # Location in which the event will take place
    venue = models.TextField(_('Event Venue'),null=True,blank=True)
    # Event costs information
    costs = models.TextField(_('Event Cost'),null=True,blank=True)
    # Picture of the event schedule
    program_picture = models.ImageField(_('Program Picture'),upload_to='img/events',null=True,blank=True)
    # Event images
    images = models.ManyToManyField('EventImage')



