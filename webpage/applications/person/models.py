from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    """
    Moel for a member, a memper is the public profile for a member of lascilab
    """
    # Profile picture
    picture = models.ImageField(_('Picture'),upload_to='img/people',null=True,blank=True)
    # Name of the member
    name = models.CharField(_('Name'),max_length=100)
    # Email of the member
    email = models.EmailField(_('Email'))
    # Github URL of the member
    github_url = models.URLField(_('Github Account URL'),null=True,blank=True)
    # google url of the member
    google_url = models.URLField(_('Google Account URL'),null=True,blank=True) 
    # youtube channer url
    youtube_channel_url = models.URLField(_('Youtube Channer URL'),null=True,blank=True) 
    # web page url
    webpage_url = models.URLField(_('Web Page URL'),null=True,blank=True) 
    # Self description of the member
    description = models.TextField(_('About Me'),null=True,blank=True)
    # Set of interest of the member
    interest = models.TextField(_('Areas of Interest'))
    # University or company
    affiliation = models.CharField(_('Affiliation'),max_length=500)
    # Laboratory
    laboratory = models.CharField(_('Laboratory'),max_length=500)
    # groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to.'
        ),
        related_name="person_set"
    )


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name