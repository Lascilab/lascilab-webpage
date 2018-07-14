# -*- encoding: utf-8 -*-

from django.urls import path

from index.views import Index
from index.views import History

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('history/', History.as_view(), name='history'),
]