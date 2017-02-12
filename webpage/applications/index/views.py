from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group

class Index(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self,**kwargs):
        context = super(Index,self).get_context_data(**kwargs)
        # members = Group.objects.get()
        members = []
        chunk_size = 3
        paired_members = [members[i:i + chunk_size] for i in range(0, len(members), chunk_size)]
        context['paired_members'] = paired_members
        return context
