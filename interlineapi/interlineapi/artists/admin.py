from django.contrib import admin

from .models import Artist, Album

# Register your models here.

artistModels = [Artist, Album]

admin.site.register(artistModels)