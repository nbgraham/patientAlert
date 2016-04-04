# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    time = models.DateTimeField(blank=True, null=True)
    doctorid = models.IntegerField(blank=True, null=True)
    patientid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class Doctor(models.Model):
    doctorid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patient(models.Model):
    patientid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'
