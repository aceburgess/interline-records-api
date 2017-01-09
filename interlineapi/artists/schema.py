from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from interlineapi.artists.models import Artist, Album

class ArtistNode(DjangoObjectType):
	class Meta:
		model = Artist
		filter_fields = ['name', 'albums']
		interfaces = (relay.Node,)


class AlbumNode(DjangoObjectType):
	class Meta:
		model = Album
		filter_fields = {
			'title': ['exact', 'icontains', 'istartswith'],
			'artist': ['exact'],
			'artist__name': ['exact'],
		}
		interfaces = (relay.Node,)


class Query(AbstractType):
	artist = relay.Node.Field(ArtistNode)
	all_artists = DjangoFilterConnectionField(ArtistNode)

	album = relay.Node.Field(AlbumNode)
	all_albums = DjangoFilterConnectionField(AlbumNode)