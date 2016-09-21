# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(null=True, upload_to=b'img', blank=True)),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('github_url', models.URLField(null=True, blank=True)),
                ('google_url', models.URLField(null=True, blank=True)),
                ('description', models.TextField()),
                ('interest', models.TextField()),
            ],
        ),
    ]
