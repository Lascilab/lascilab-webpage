from django.conf.urls import include, url
from .views import EventList, EventDetail


urlpatterns = [
    url(r'^event/list/$', EventList.as_view(), name='list'),
    url(r'^event/detail/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'), 
]