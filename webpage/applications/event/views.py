from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Event


class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event

    def get_context_data(self,**kwargs):
    	context = super(EventDetail,self).get_context_data(**kwargs)
    	context['event_list'] = Event.objects.all()
    	return context 
