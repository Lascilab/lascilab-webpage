from django.conf.urls import include, url
from .views import EventList


urlpatterns = [
    url(r'^event/list/$', EventList.as_view(), name='list'),
]