# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from person.models import Person
from datetime import date


class Topic(models.Model):
    """
    A topic, presentation or workshop that will be presented
    during the event. 
    """

    # Name for the topic
    name = models.CharField(_('Topic'),max_length=400)
    # Brief description
    description = models.TextField(_('Description'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):
    """
    Sponsor of the event
    """

    # Name
    name = models.CharField(_('Name'),max_length=400,null=True,blank=True)
    # Sponsor's logo
    image = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)
    
    def __str__(self):
        return self.name or "without name"

    def __unicode__(self):
        return self.name or "without name"


class Memory(models.Model):
    """
    Event memories
    """

    seminar = models.ForeignKey('Seminar', on_delete=models.CASCADE)
    image = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)


class Seminar(models.Model):
    """
    A conference or other meeting for discussion or training.
    """

    name = models.CharField(_('Name'),max_length=400,null=True,blank=True)
    # Event banner or picture (preferably in PNG format)
    banner = models.ImageField(_('Image'),null=True, blank=True, help_text='preferably in PNG format')
    # Important notes about the event
    important_notes = models.TextField(_('Important Notes'),null=True,blank=True)
    # Important dates about the event
    application_opening = models.DateField(_('Application Opening'))
    application_deadline = models.DateField(_('Application Deadline'))
    admission_notification = models.DateField(_('Admission Notification'),null=True,blank=True)
    start_date = models.DateTimeField(_('Start Date'),null=True,blank=True)
    end_date = models.DateTimeField(_('End Date'),null=True,blank=True)
    # Registration link
    registration_form_url = models.URLField(_('Registration Form URL'),null=True,blank=True)
    # Feedback form url
    feedback_form_url = models.URLField(_('Feedback Form URL'),null=True,blank=True)
    # The Objective of the event
    mission = models.TextField(_('Event Mision'),null=True,blank=True)
    # Google docs exel with the event schedule.
    program_url = models.URLField(_('Program URL'),null=True,blank=True)    # Description of the activity
    # Event speakers
    speakers = models.ManyToManyField(Person,blank=True)
    # Event's topics
    topics = models.ManyToManyField('Topic')
    # Location in which the event will take place
    venue = models.TextField(_('Venue'),null=True,blank=True)
    # Event costs information
    costs = models.TextField(_('Cost'),null=True,blank=True)
    # Sponsors
    sponsors = models.ManyToManyField('Sponsor',blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def is_application_open(self):
        return date.today() >= self.application_opening and date.today() < self.application_deadline 
