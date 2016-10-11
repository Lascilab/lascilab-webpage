from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	#atributos
	
	list_display = (
		'id', 'picture', 'name','email', 
		'github_url', 'google_url', 'youtube_channel_url','webpage_url',
		'description','interest')
	search_fields = ('name', 'id')
	  
# Register your models here.
admin.site.register(Member, MemberAdmin)

