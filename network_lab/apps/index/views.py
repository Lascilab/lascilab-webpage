from django.shortcuts import render
from django.views.generic import TemplateView
from network_lab.apps.members.models import Member
# Create your views here.

class Index(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self,**kwargs):
    	context = super(Index,self).get_context_data(**kwargs)
    	context['members'] = Member.objects.all()
    	return context