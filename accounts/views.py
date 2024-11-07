from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Welcome to Aeroponics!</h1>")
