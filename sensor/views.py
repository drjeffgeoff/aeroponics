from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SensorData
from .serializers import SensorDataSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]


# sensor/views.py


def index(request):
    return HttpResponse("Welcome to the Sensor app!")
