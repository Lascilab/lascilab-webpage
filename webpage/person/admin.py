# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from person.models import Person, Contribution


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','email','status')
    fieldsets = (
        (_('Personal info'), {'fields': ('picture', 'name', 'email','description')}),
        (_('Pages'), {'fields': ('github_url',)}),
        (_('Schoolar'), {'fields': ('interest', 'affiliation','laboratory','status')}),
    )
    search_fields = ('name',)
    list_filter = ('name','email','status')

admin.site.register(Person,PersonAdmin)

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('title','abstract','ctype')
    search_fields = ('title','ctype')
    list_filter = ('title','ctype')

admin.site.register(Contribution,ContributionAdmin)
