# -*- encoding: utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from event.models import Seminar


class SeminarList(ListView):
    model = Seminar

class SeminarDetail(DetailView):
    model = Seminar
