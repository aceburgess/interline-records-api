from interlineapi.artists.models import Artist, Album, Video
from interlineapi.general.models import SiteSetting, Announcement
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'
		# fields = ('id', 'title', 'artist', 'release_date')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		fields = '__all__'

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	albums = AlbumSerializer(many=True, read_only=True)
	videos = VideoSerializer(many=True, read_only=True)

	class Meta:
		model = Artist
		# fields = ('id', 'name', 'biography', 'website', 'albums', 'photo')
		fields = '__all__'

class SiteSettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SiteSetting
		fields = '__all__'

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	artist = ArtistSerializer(read_only=True)
	album = AlbumSerializer(read_only=True)
	video = VideoSerializer(read_only=True)

	class Meta:
		model = Announcement
		fields = '__all__'