from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response

class APIRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'Data': {
                'Appointments': reverse('appointment-list', request=request),
                'Doctors': reverse('doctor-list', request=request),
                'Patients': reverse('patient-list', request=request),
            }
        })
