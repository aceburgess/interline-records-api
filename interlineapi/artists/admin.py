from django.contrib import admin

from .models import Artist, Album

# Register your models here.

artist_models = [Artist, Album]

admin.site.register(artist_models)