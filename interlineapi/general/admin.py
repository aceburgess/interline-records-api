from django.contrib import admin

from .models import SiteSetting, Announcement

# Register your models here.

general_models = [SiteSetting, Announcement]

admin.site.register(general_models)
