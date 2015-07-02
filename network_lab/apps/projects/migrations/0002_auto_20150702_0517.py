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
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='members.Member'),
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
