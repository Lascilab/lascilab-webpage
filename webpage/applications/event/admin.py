from django.contrib import admin
from .models import Event, Topic, EventImage, Sponsor, EventSpeaker
from django.utils.translation import ugettext_lazy as _

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'application_opening',
        'application_deadline',
        'admission_notification',
        'start_date',
        'end_date')

    fieldsets = (
        (_('Overview'), 
            {'fields': (
                'banner', 
                'important_notes',
                'mision',
                'program',
                'venue',
                'costs',
                'registration_form_url',
                'feedback_form_url')}),
        (_('Dates'), 
            {'fields': (
            'application_opening',
            'application_deadline',
            'admission_notification',
            'start_date',
            'end_date')}),
        (_('Images'), {'fields': ('images',)}),
        (_('Sponsors'), {'fields': ('sponsors',)}),
    )
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Event,EventAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Topic,TopicAdmin)

class EventImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(EventImage,EventImageAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

admin.site.register(Sponsor,SponsorAdmin)

class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ('event','speaker')

admin.site.register(EventSpeaker,EventSpeakerAdmin)
