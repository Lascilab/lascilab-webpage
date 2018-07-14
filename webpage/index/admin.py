from django.contrib import admin

from index.models import BannerImage


class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('id','image','detail_url')

admin.site.register(BannerImage,BannerImageAdmin)
