# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    """
    Model for a member, a memper is the public profile for a member of lascilab
    """

    STUDENT = 'Student'
    GRADUATED = 'Graduated'
    ASSOCIATE = 'Associated'
    COORDINATOR = 'Coordinator'

    STATUS = (
        (STUDENT, 'Student'),
        (GRADUATED, 'Graduated'),
        (ASSOCIATE, 'Associated'),
        (COORDINATOR, 'Coordinator'),
    )


    # Profile picture
    picture = models.ImageField(_('Picture'),upload_to='img/people',null=True,blank=True)
    # Name of the member
    name = models.CharField(_('Name'),max_length=100)
    # Email of the member
    email = models.EmailField(_('Email'))
    # Github URL of the member
    github_url = models.URLField(_('Github Account URL'),null=True,blank=True)
    # Self description of the member and areas of interest
    description = models.TextField(_('About Me'),null=True,blank=True)
    # Specific interest area
    interest = models.CharField(_('Specific Area of Interest'), max_length=200)
    # University or company
    affiliation = models.CharField(_('Affiliation'),max_length=500)
    # Laboratory
    laboratory = models.CharField(_('Laboratory'),max_length=500)
    # Status
    status = models.CharField(
        _('Status'),
        max_length=20,
        choices=STATUS,
        default=STUDENT,
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Contribution(models.Model):
    """
    Contributions that a person give to the laboratory, 
    research practices and thesis. Other informations like 
    pappers, etc is not relevant here because it can be placed
    in a curriculum vitae.
    """

    BSC_TESIS = 'BSc. Thesis'
    MSC_THESIS = 'MSc. Thesis'
    PHD_THESIS = 'PhD. Thesis'
    BSC_TESIS_M = 'Meritorious - BSc. Thesis'
    MSC_THESIS_M = 'Meritorious - MSc. Thesis'
    PHD_THESIS_M = 'Meritorious - PhD. Thesis'
    PRACTICE = 'Research Practice'
    
    TYPE = (
        (BSC_TESIS, 'BSc. Thesis'),
        (MSC_THESIS, 'MSc. Thesis'),
        (PHD_THESIS, 'PhD. Thesis'),
        (BSC_TESIS_M, 'Meritorious - BSc. Thesis'),
        (MSC_THESIS_M, 'Meritorious - MSc. Thesis'),
        (PHD_THESIS_M, 'Meritorious - PhD. Thesis'),
        (PRACTICE, 'Research Practice'),
    )

    # The person that makes the contribution
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # Name if the contribution: research practice or thesis
    title = models.CharField(_('Title'),max_length=800)
    # An overview for the contribution
    abstract = models.TextField(_('Abstract'),null=True,blank=True)
    # Type of the contribution
    ctype = models.CharField(
        _('Contribution type'),
        max_length=30,
        choices=TYPE,
        default=BSC_TESIS,
    )

