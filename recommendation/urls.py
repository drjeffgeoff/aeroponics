
# recommendation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recommendation_index'),  # Example route
]
