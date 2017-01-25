# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20170125_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='registration_url',
        ),
        migrations.AddField(
            model_name='event',
            name='feedback_form_url',
            field=models.URLField(blank=True, null=True, verbose_name='Feedback Form URL'),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_form_url',
            field=models.URLField(blank=True, null=True, verbose_name='Registration Form URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=400, verbose_name='Topic'),
        ),
    ]
