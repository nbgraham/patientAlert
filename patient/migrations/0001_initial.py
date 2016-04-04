# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('doctorid', models.IntegerField(blank=True, null=True)),
                ('patientid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'patient',
            },
        ),
    ]