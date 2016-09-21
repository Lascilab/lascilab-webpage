# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=100, null=True, blank=True)),
                ('link', models.URLField()),
                ('members', models.ManyToManyField(to='members.Member')),
                ('topics', models.ManyToManyField(to='projects.Topic')),
            ],
        ),
    ]
