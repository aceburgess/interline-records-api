from django.contrib.auth.models import User, Group
from interlineapi.artists.models import Artist, Album, Video
from interlineapi.general.models import SiteSetting, Announcement, Staff, Company
from rest_framework import viewsets
from interlineapi.serializers import \
	ArtistSerializer, AlbumSerializer, VideoSerializer, \
	SiteSettingSerializer, AnnouncementSerializer, \
	StaffSerializer, CompanySerializer

class ArtistViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows artists to be viewed / edited.
	"""
	queryset = Artist.objects.filter(display=True)
	serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows albums to be viewed / edited.
	"""
	queryset = Album.objects.filter(display=True)
	serializer_class = AlbumSerializer

class VideoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows videos to be viewed / edited.
	"""
	queryset = Video.objects.filter(display=True)
	serializer_class = VideoSerializer

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
	queryset = Announcement.objects.filter(display=True)
	serializer_class = AnnouncementSerializer

class StaffViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Staff to be viewed
	"""
	queryset = Staff.objects.filter(display=True)
	serializer_class = StaffSerializer

class CompanyViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Staff to be viewed
	"""
	queryset = Company.objects.filter(display=True)
	serializer_class = CompanySerializer