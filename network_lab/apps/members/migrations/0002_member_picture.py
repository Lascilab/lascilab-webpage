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
            name='picture',
            field=models.ImageField(default=None, upload_to=b'img'),
            preserve_default=False,
        ),
    ]
