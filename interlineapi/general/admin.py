from django.contrib import admin

from .models import SiteSetting, Announcement, Staff, Company

# Register your models here.

general_models = [Company, Staff, SiteSetting]


class AnnouncementAdmin(admin.ModelAdmin):
	model = Announcement

	search_fields = ['artist__name', 'album__title', 'video__title']
	ordering = ('-created_at',)
	list_display = ('display', 'announcement',)

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(general_models)
