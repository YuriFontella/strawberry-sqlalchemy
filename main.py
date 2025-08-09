from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from src.infrastructure.container import Container
from src.infrastructure.config.settings import get_settings
from src.infrastructure.database.session import create_tables
from src.presentation.graphql.schema import create_schema
from src.presentation.graphql.context import GraphQLContext


def create_app() -> FastAPI:
    """Cria a aplicação FastAPI com Clean Architecture"""

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
        return GraphQLContext(
            artist_resolvers=container.artist_resolvers,
            music_resolvers=container.music_resolvers,
        )

    # GraphQL Router
    graphql_app = GraphQLRouter(schema, context_getter=get_context)

    # Aplicação
    fastapi = FastAPI(debug=settings.debug)

    # Configuração CORS
    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Adiciona rota GraphQL
    fastapi.include_router(graphql_app, prefix="/graphql")

    return fastapi


# Instância da aplicação
app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
