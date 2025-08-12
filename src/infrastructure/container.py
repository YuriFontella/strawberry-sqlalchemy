from dependency_injector import containers, providers
from src.presentation.graphql.context import GraphQLContext
from src.application.use_cases.artist_use_cases import ArtistUseCases
from src.application.use_cases.music_use_cases import MusicUseCases
from src.presentation.graphql.artist.resolver import ArtistResolvers
from src.presentation.graphql.music.resolver import MusicResolvers
from src.infrastructure.database.repositories.artist_repository import (
    SQLAlchemyArtistRepository,
)
from src.infrastructure.database.repositories.music_repository import (
    SQLAlchemyMusicRepository,
)


class Container(containers.DeclarativeContainer):
    """Container de injeção de dependências usando dependency-injector"""

    # Repositories
    artist_repository = providers.Singleton(SQLAlchemyArtistRepository)
    music_repository = providers.Singleton(SQLAlchemyMusicRepository)

    # Use Cases
    artist_use_cases = providers.Factory(
        ArtistUseCases, artist_repository=artist_repository
    )

    music_use_cases = providers.Factory(
        MusicUseCases, music_repository=music_repository
    )

    # Resolvers
    artist_resolvers = providers.Factory(
        ArtistResolvers, artist_use_cases=artist_use_cases
    )

    music_resolvers = providers.Factory(MusicResolvers, music_use_cases=music_use_cases)

    # Contexto do GraphQL
    graphql_context = providers.Factory(
        GraphQLContext,
        artist_resolvers=artist_resolvers,
        music_resolvers=music_resolvers,
    )
