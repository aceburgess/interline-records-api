from django.contrib import admin

from .models import SiteSetting, Announcement, Staff, Company

# Register your models here.

general_models = [Company, Staff, Announcement, SiteSetting]

admin.site.register(general_models)
