# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20170124_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'img/events', null=True, verbose_name='Picture', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='Event Topic')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='encharged',
        ),
        migrations.RemoveField(
            model_name='event',
            name='place',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='admission_notification',
            field=models.DateField(null=True, verbose_name='Admission Notification', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='application_deadline',
            field=models.DateField(null=True, verbose_name='Application Deadline', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='application_opening',
            field=models.DateField(null=True, verbose_name='Application Opening', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='banner',
            field=models.ImageField(upload_to=b'img/events', null=True, verbose_name='Picture', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='costs',
            field=models.TextField(null=True, verbose_name='Event Cost', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='important_notes',
            field=models.TextField(null=True, verbose_name='Important Notes', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='mision',
            field=models.TextField(null=True, verbose_name='Event Mision', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.CharField(max_length=100, null=True, verbose_name='Event Organization', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='program_picture',
            field=models.ImageField(upload_to=b'img/events', null=True, verbose_name='Program Picture', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_deadline',
            field=models.DateField(null=True, verbose_name='Registration Deadline', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.TextField(null=True, verbose_name='Event Venue', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='event.EventImage'),
        ),
        migrations.AddField(
            model_name='event',
            name='topics',
            field=models.ManyToManyField(to='event.Topics'),
        ),
    ]
