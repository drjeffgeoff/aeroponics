# crop_monitoring/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='crop_monitoring_index'),  # Example view
]
