from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from random import shuffle

class Index(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self,**kwargs):
        context = super(Index,self).get_context_data(**kwargs)
        try:
	    group = Group.objects.get(name='Member')
	    members = list(group.person_set.all())
            shuffle(members)
            chunk_size = 3
            paired_members = [members[i:i + chunk_size] for i in range(0, len(members), chunk_size)]
            context['paired_members'] = paired_members
	except Exception:
            context['paired_members'] = []

	return context
