# -*- encoding: utf-8 -*-

from django.urls import path

from event.views import SeminarList
from event.views import SeminarDetail

urlpatterns = [
    path('seminars/', SeminarList.as_view(), name='seminars'),
    path('seminar/<int:pk>/', SeminarDetail.as_view(), name='seminar'),
]