from django.contrib.auth.models import User, Group
from interlineapi.artists.models import Artist, Album
from rest_framework import viewsets
from interlineapi.serializers import ArtistSerializer, AlbumSerializer

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