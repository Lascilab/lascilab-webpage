# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150702_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='topics',
            field=models.ManyToManyField(to='projects.Topic'),
        ),
    ]
