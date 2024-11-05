from django.db import models
from accounts.models import User


class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pH = models.FloatField()
    light_intensity = models.FloatField()
    nutrient_level = models.FloatField()

    def __str__(self):
        return f"Data from {self.user} at {self.timestamp}"
