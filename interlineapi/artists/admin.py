from django.contrib import admin

from .models import Artist, Album, Video
from interlineapi.general.models import Announcement

# Register your models here.

def make_public(modeladmin, request, queryset):
	queryset.update(display=True)

make_public.short_description = 'Make selected public'

def make_not_public(modeladmin, request, queryset):
	queryset.update(display=False)

make_not_public.short_description = 'Make selected NOT public'

class AnnouncementInline(admin.TabularInline):
	model = Announcement
	extra = 1

	fields = ('display', 'announcement','link',)

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 1

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1

class AlbumAdmin(admin.ModelAdmin):
	model = Album

	search_fields = ['title', 'artist__name']
	ordering = ('-release_date','artist')
	# list_editable = ('display',)
	list_display = ('display', 'title', 'artist', 'release_date',)
	list_display_links = ('display', 'title',)
	list_filter = ('artist__name','display',)
	actions = [make_public, make_not_public]

	inlines = [
		AnnouncementInline,
	]

class VideoAdmin(admin.ModelAdmin):
	model = Video

	search_fields = ['title', 'artist__name']
	ordering = ('-updated_at','artist')
	list_display = ('display', 'title', 'artist','updated_at',)
	list_display_links = ('display', 'title',)
	list_filter = ('artist__name','display',)
	actions = [make_public, make_not_public]

	inlines = [
		AnnouncementInline,
	]

class ArtistAdmin(admin.ModelAdmin):
	model = Artist

	prepopulated_fields = {'slug': ('name',)}

	list_display = ('display', 'name', 'created_at', 'updated_at',)
	ordering = ('-updated_at', 'name',)
	list_display_links = ('display', 'name',)
	list_filter = ('display',)

	inlines = [
		AnnouncementInline,
		AlbumInline,
		VideoInline,
	]

	actions = [make_public, make_not_public]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Video, VideoAdmin)