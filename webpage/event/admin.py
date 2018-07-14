# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import *


class SeminarAdmin(admin.ModelAdmin):
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
                'mission',
                'venue',
                'costs',
                'program_url',
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
        (_('Sponsors'), {'fields': ('sponsors',)}),
        (_('Speakers'), {'fields': ('speakers',)}),
    )
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Seminar,SeminarAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Topic,TopicAdmin)

class MemoryAdmin(admin.ModelAdmin):
    list_display = ('seminar','image',)

admin.site.register(Memory,MemoryAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(Sponsor,SponsorAdmin)
