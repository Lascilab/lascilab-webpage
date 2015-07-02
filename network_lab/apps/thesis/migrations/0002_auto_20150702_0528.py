# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_topics'),
        ('members', '0001_initial'),
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='author',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='director',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='topic',
        ),
        migrations.AddField(
            model_name='thesis',
            name='members',
            field=models.ManyToManyField(to='members.Member'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='topics',
            field=models.ManyToManyField(to='projects.Topic'),
        ),
    ]
