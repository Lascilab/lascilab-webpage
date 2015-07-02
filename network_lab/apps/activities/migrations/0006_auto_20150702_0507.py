# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20150702_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='encharged1',
            new_name='encharged',
        ),
    ]
