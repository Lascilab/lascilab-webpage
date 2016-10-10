# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('horary', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('initial_date', models.DateField(null=True, blank=True)),
                ('final_date', models.DateField(null=True, blank=True)),
                ('teacher', models.ForeignKey(blank=True, to='members.Member', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('type', models.CharField(max_length=20)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
    ]
