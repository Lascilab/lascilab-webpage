# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='encharged',
        ),
    ]
