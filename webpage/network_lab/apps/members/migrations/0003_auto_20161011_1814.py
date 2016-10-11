# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20161011_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
