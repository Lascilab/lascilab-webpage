# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20150702_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='encharged',
            field=models.ForeignKey(blank=True, to='members.Member', null=True),
        ),
    ]
