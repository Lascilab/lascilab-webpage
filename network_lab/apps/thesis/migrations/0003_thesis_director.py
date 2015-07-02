# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0002_auto_20150702_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='director',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
