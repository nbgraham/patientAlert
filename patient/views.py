from rest_framework import viewsets
from patient.models import Appointment, Doctor, Patient
from patient.serializers import AppointmentSerializer, DoctorSerializer, PatientSerializer
from .filters import AppointmentFilter

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    model = Appointment
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_class = AppointmentFilter
    ordering_fields = '__all__'


class PatientViewSet(viewsets.ModelViewSet):
    model = Patient
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    model = Doctor
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
