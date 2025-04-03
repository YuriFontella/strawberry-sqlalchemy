import strawberry

from gql.resolvers.ouvidoria import post_ouvidoria


@strawberry.type
class OuvidoriaMutation:
    add_ouvidoria: bool = strawberry.field(resolver=post_ouvidoria)
