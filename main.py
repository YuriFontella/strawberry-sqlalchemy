from litestar import Litestar
from litestar.config.cors import CORSConfig
from strawberry.litestar import make_graphql_controller
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from src.infrastructure.container import Container
from src.infrastructure.config.settings import get_settings
from src.infrastructure.database.session import create_tables
from src.presentation.graphql.schema import create_schema
from src.presentation.graphql.context import GraphQLContext


def create_app() -> Litestar:
    """Cria a aplicação Litestar com Clean Architecture"""
    
    # Configurações
    settings = get_settings()
    
    # Container de dependências
    container = Container()
    
    # Criar tabelas do banco
    create_tables()
    
    # Schema GraphQL
    schema = create_schema()
    
    # Contexto do GraphQL
    async def get_context():
        return {
            "artist_resolvers": container.artist_resolvers,
            "music_resolvers": container.music_resolvers
        }
    
    # Controller GraphQL
    graphql_controller = make_graphql_controller(
        schema=schema,
        path='/graphql',
        context_getter=get_context
    )
    
    # Configuração CORS
    cors_config = CORSConfig(allow_origins=settings.cors_origins)
    
    # Aplicação
    litestar = Litestar(
        route_handlers=[graphql_controller],
        cors_config=cors_config,
        debug=settings.debug
    )
    
    return litestar


# Instância da aplicação
app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
