from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Event

class EventList(ListView):
    model = Event
    