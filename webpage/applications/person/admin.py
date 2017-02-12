from django.contrib import admin
from .models import Person
from django.utils.translation import ugettext_lazy as _

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    fieldsets = (
        (_('Personal info'), {'fields': ('picture', 'name', 'email','description')}),
        (_('Pages'), {'fields': ('github_url', 'google_url','youtube_channel_url', 'webpage_url')}),
        (_('Schoolar'), {'fields': ('interest', 'affiliation','laboratory')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    search_fields = ('name',)
    list_filter = ('name','email')

admin.site.register(Person,PersonAdmin)