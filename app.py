import strawberry

from litestar import Litestar
from litestar.config.cors import CORSConfig

from strawberry.litestar import make_graphql_controller

from gql.schema.ouvidoria import OuvidoriaMutation
from gql.schema.ludopatia import LudopatiaMutation
from gql.schema.root import RootQuery

from middlewares.on_startup import create_all

cors_config = CORSConfig(allow_origins=['*'])


@strawberry.type
class Query(RootQuery):
    pass


@strawberry.type
class Mutation(OuvidoriaMutation, LudopatiaMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

GraphQLController = make_graphql_controller(
    schema=schema,
    path='/graphql'
)

app = Litestar(route_handlers=[GraphQLController], cors_config=cors_config, on_startup=[create_all])
