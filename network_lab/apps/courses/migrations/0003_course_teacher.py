# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('courses', '0002_auto_20150620_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
        ),
    ]
