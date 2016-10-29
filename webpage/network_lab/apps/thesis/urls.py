from django.conf.urls import include, url

from .views import Index #, Docker
urlpatterns = [
    url(r'^$', Index.as_view(), name='index-thesis'),
    #url(r'^create$', Docker.as_view(), name='condor'),
]
