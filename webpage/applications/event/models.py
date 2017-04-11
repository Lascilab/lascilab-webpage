from __future__ import unicode_literals

from django.db import models
from applications.person.models import Person
from django.utils.translation import ugettext_lazy as _
from datetime import date


class Topic(models.Model):
    name = models.CharField(_('Topic'),max_length=400)
    description = models.TextField(_('Description'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(_('Image Name'),max_length=400)
    image = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)

    def __str__(self):
        return self.name or "without name"

    def __unicode__(self):
        return self.name or "without name"


class Sponsor(models.Model):
    name = models.CharField(_('Name'),max_length=400,null=True,blank=True)
    image = models.ImageField(_('Picture'),upload_to='img/events',null=True,blank=True)
    
    def __str__(self):
        return self.name or "without name"

    def __unicode__(self):
        return self.name or "without name"


class Event(models.Model):
    """
    An event is sleep, and I don't like to document at midnigth
    """
    name = models.CharField(_('Name'),max_length=400,null=True,blank=True)
    # Event banner or picture
    banner = models.ImageField(_('Image'))
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
    mision = models.TextField(_('Event Mision'),null=True,blank=True)
    # Description of the activity
    topics = models.ManyToManyField('Topic')
    # Location in which the event will take place
    venue = models.TextField(_('Venue'),null=True,blank=True)
    # Event costs information
    costs = models.TextField(_('Cost'),null=True,blank=True)
    # Picture of the event schedule
    program = models.URLField(_('Program URL'),null=True,blank=True)
    # Event images
    images = models.ManyToManyField('Image',blank=True)
    # Sponsors
    sponsors = models.ManyToManyField('Sponsor',blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def is_application_open(self):
        return date.today() >= self.application_opening and date.today() < self.application_deadline 


class Speaker(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    topics = models.ManyToManyField('Topic')

    def __str__(self):
        return self.person.name + ', ' + self.event.name

    def __unicode__(self):
        return self.person.name + ', ' + self.event.name
