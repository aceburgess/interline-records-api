from interlineapi.artists.models import Artist, Album, Video
from interlineapi.general.models import SiteSetting, Announcement, Staff, Company
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'
		depth = 1
		# fields = ('id', 'title', 'artist', 'release_date')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		fields = '__all__'
		depth = 1

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
	# artist = ArtistSerializer(read_only=True)
	# album = AlbumSerializer(read_only=True)
	# video = VideoSerializer(read_only=True)

	class Meta:
		model = Announcement
		fields = '__all__'
		depth = 2

class StaffSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Staff
		fields = '__all__'

class CompanySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'