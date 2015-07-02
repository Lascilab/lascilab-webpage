# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('activities', '0004_auto_20150702_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='encharged',
        ),
        migrations.AddField(
            model_name='activity',
            name='encharged1',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
        ),
    ]
