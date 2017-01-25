from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Event


class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event
