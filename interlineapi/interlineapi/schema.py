import graphene

import interlineapi.artists.schema


class Query(interlineapi.artists.schema.Query, graphene.ObjectType):

	pass

schema = graphene.Schema(query=Query)