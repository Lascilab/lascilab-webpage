# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='webpage_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='youtube_channel_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
