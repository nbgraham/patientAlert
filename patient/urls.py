from rest_framework import routers
from patient.views import AppointmentViewSet, PatientViewSet, DoctorViewSet
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.SimpleRouter()
router.register('appointments', AppointmentViewSet)
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
