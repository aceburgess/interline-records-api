from interlineapi.artists.models import Artist, Album
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('id', 'name', 'biography', 'website', 'albums', 'photo')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = ('id', 'title', 'artist', 'release_date')