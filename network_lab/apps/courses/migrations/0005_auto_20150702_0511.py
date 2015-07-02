# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_encharged'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='final_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='initial_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
    ]
