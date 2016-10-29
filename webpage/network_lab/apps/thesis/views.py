from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,View
#from getname import random_name
#from docker import Client
#import string
#import datetime

# Create your views here.

class Index(TemplateView):
    template_name = 'thesis/index.html'
