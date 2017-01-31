from django.contrib import admin
from .models import Event, Topic, EventImage, Sponsor


admin.site.register(Event)
admin.site.register(Topic)
admin.site.register(EventImage)
admin.site.register(Sponsor)
