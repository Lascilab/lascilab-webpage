# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='registration_deadline',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Event Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_url',
            field=models.URLField(blank=True, null=True, verbose_name='Registration URL'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
