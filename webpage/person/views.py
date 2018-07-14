# -*- encoding: utf-8 -*-


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from person.models import Person

class PersonList(ListView):

    model = Person
    template_name = 'person/person_list.html'

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['are_there_students'] = self.get_queryset().exclude(status='Associated').exclude(status='Graduated').count()
        context['are_there_associated'] = self.get_queryset().filter(status='Associated').count()
        context['are_there_graduated'] = self.get_queryset().filter(status='Graduated').count()
        return context


class PersonDetail(DetailView):

	model = Person
	template_name = 'person/person_detail.html'