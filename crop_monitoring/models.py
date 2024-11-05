from django.db import models
from sensor.models import SensorData


class Crop(models.Model):
    name = models.CharField(max_length=100)
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE)
    growth_stage = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
