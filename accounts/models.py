from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('technician', 'Technician')
    ]

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='farmer')

    # Override groups and user_permissions fields with unique related names
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )
