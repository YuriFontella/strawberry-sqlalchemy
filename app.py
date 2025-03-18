import strawberry

from litestar import Litestar
from litestar.config.cors import CORSConfig

from strawberry.litestar import make_graphql_controller
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from gql.schema.artist import ArtistQuery, ArtistMutation
from gql.schema.music import MusicQuery, MusicMutation
from gql.schema.subscription import Subscription

from middlewares.on_startup import create_all

cors_config = CORSConfig(allow_origins=['*'])


@strawberry.type
class Query(ArtistQuery, MusicQuery):
    pass


@strawberry.type
class Mutation(ArtistMutation, MusicMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

GraphQLController = make_graphql_controller(
    schema=schema,
    path='/graphql',
    subscription_protocols=(GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL)
)

app = Litestar(route_handlers=[GraphQLController], cors_config=cors_config, on_startup=[create_all])
