from django.contrib.auth.models import User, Group
from interlineapi.artists.models import Artist, Album
from interlineapi.general.models import SiteSetting, Announcement
from rest_framework import viewsets
from interlineapi.serializers import ArtistSerializer, AlbumSerializer, SiteSettingSerializer, AnnouncementSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows artists to be viewed / edited.
	"""
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows albums to be viewed / edited.
	"""
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class SiteSettingViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Site Settings to be viewed
	"""
	queryset = SiteSetting.objects.all()
	serializer_class = SiteSettingSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Announcements to be viewed
	"""
	queryset = Announcement.objects.all()
	serializer_class = AnnouncementSerializer