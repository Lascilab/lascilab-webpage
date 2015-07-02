# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_topics'),
        ('members', '0001_initial'),
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='members',
            field=models.ManyToManyField(to='members.Member'),
        ),
        migrations.AddField(
            model_name='research',
            name='topics',
            field=models.ManyToManyField(to='projects.Topic'),
        ),
    ]
