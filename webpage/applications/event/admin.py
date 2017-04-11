from django.contrib import admin
from .models import *
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
	        'name',
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
        (_('Syllabus'), {'fields': ('topics',)}),
        (_('Images'), {'fields': ('images',)}),
        (_('Sponsors'), {'fields': ('sponsors',)}),
    )
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Event,EventAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Topic,TopicAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(Image,ImageAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(Sponsor,SponsorAdmin)

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('event','person')

admin.site.register(Speaker,SpeakerAdmin)
