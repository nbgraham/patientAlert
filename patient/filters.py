__author__ = 'Nicholas'

import django_filters
from .models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    min_time = django_filters.DateFilter(name='time', lookup_type='gte')
    max_time = django_filters.DateFilter(name='time', lookup_type='lte')
    patientid = django_filters.CharFilter(lookup_type='icontains')
    doctorid = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
            model = Appointment
            fields = ['patientid', 'doctorid',]

