from django.core.management.base import BaseCommand
from sensor.models import SensorData
import random
from django.utils import timezone


class Command(BaseCommand):
    help = "Generate random sensor data"

    def handle(self, *args, **kwargs):
        SensorData.objects.create(
            user_id=1,  # Assume a test user
            temperature=random.uniform(18.0, 25.0),
            humidity=random.uniform(60.0, 80.0),
            pH=random.uniform(5.5, 6.5),
            light_intensity=random.uniform(300, 700),
            nutrient_level=random.uniform(0.8, 1.2),
            timestamp=timezone.now()
        )
        self.stdout.write(self.style.SUCCESS("Generated random sensor data."))
