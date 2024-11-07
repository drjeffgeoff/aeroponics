# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts_index'),  # Example view
]
