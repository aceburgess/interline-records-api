from interlineapi.artists.models import Artist, Album
from interlineapi.general.models import SiteSetting, Announcement
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		# fields = ('id', 'name', 'biography', 'website', 'albums', 'photo')
		fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'
		# fields = ('id', 'title', 'artist', 'release_date')

class SiteSettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SiteSetting
		fields = '__all__'

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Announcement
		fields = '__all__'