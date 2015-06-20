# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('descripcion', models.TextField()),
                ('titulo', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
            ],
        ),
    ]
