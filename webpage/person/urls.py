# -*- encoding: utf-8 -*-

from django.urls import path

from person.views import PersonList, PersonDetail

urlpatterns = [
    path('members/', PersonList.as_view(), name='members'),
    path('member/<int:pk>/', PersonDetail.as_view(), name='member'),
]