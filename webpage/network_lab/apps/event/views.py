from django.views.generic import ListView
from .models import Event

class EventList(ListView):
    model = Event
    