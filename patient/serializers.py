from rest_framework import serializers
from patient.models import Appointment, Doctor, Patient

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('url', 'id', 'time', 'doctorid', 'patientid')

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('url', 'doctorid', 'name')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('url', 'patientid', 'name', 'phone_number')
