import os
import strawberry

from litestar import Litestar

from strawberry.litestar import make_graphql_controller
from strawberry.extensions import AddValidationRules

from graphql.validation import NoSchemaIntrospectionCustomRule

from gql.schema.ouvidoria import OuvidoriaMutation
from gql.schema.ludopatia import LudopatiaMutation
from gql.schema.root import RootQuery

from middlewares.on_startup import create_all
from middlewares.util import cors_config, compression_config, rate_limit_config

is_prod = os.environ.get("PYTHON_ENV") == "production"


@strawberry.type
class Query(RootQuery):
    pass


@strawberry.type
class Mutation(OuvidoriaMutation, LudopatiaMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[AddValidationRules([NoSchemaIntrospectionCustomRule] if is_prod else [])]
)

GraphQLController = make_graphql_controller(
    schema=schema,
    path='/graphql',
    graphiql= not is_prod,
    allow_queries_via_get=not is_prod
)

app = Litestar(
    route_handlers=[GraphQLController],
    cors_config=cors_config,
    compression_config=compression_config,
    middleware=[rate_limit_config.middleware],
    on_startup=[create_all]
)
