from django.conf.urls import include, url
from django.contrib import admin

from network_lab.apps.index import urls as indexurls
from network_lab.apps.activities import urls as activitiesurls
from network_lab.apps.courses import urls as coursesurls
from network_lab.apps.members import urls as membersurls
from network_lab.apps.projects import urls as projectsurls
from network_lab.apps.research import urls as researchurls
from network_lab.apps.resources import urls as resourcesurls
from network_lab.apps.thesis import urls as thesisurls
from network_lab.apps.blog_engine import urls as blog_urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'network_lab.views.home', name='home'),
    # url(r'^blog_engine/', include('blog_engine.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(indexurls)),
    url(r'^actividades/', include(activitiesurls)),
    url(r'^cursos/', include(coursesurls)),
    url(r'^miembros/', include(membersurls)),
    url(r'^proyectos/', include(projectsurls)),
    url(r'^investigacion/', include(researchurls)),
    url(r'^recursos/', include(resourcesurls)),
    url(r'^tesis/', include(thesisurls)),
    url(r'^blog/', include(blog_urls, namespace="blog_engine")),
]
