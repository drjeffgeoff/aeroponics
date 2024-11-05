from django.db import models


class CropRecommendation(models.Model):
    crop_name = models.CharField(max_length=100)
    optimal_ph = models.FloatField()
    optimal_temp = models.FloatField()
    nutrient_requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.crop_name
