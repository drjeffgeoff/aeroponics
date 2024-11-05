from django.contrib.auth.models import AbstractUser
from django.db import models

# Define a custom User model to handle different roles (admin, farmer, technician):


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('technician', 'Technician')
    ]
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='farmer')
