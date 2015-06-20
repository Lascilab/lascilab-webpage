# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='fecha_creacion',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='encargado',
            new_name='encharged',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='lugar',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='hora',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='titulo',
            new_name='title',
        ),
    ]
