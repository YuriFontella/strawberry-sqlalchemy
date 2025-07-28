from src.domain.repositories.artist_repository import ArtistRepository
from src.domain.repositories.music_repository import MusicRepository
from src.application.use_cases.artist_use_cases import ArtistUseCases
from src.application.use_cases.music_use_cases import MusicUseCases
from src.presentation.graphql.resolvers import ArtistResolvers, MusicResolvers
from src.infrastructure.database.repositories import SQLAlchemyArtistRepository, SQLAlchemyMusicRepository


class Container:
    """Container de injeção de dependências"""

    def __init__(self):
        # Repositórios
        self._artist_repository: ArtistRepository = SQLAlchemyArtistRepository()
        self._music_repository: MusicRepository = SQLAlchemyMusicRepository()

        # Casos de uso
        self._artist_use_cases = ArtistUseCases(self._artist_repository)
        self._music_use_cases = MusicUseCases(self._music_repository)

        # Resolvers
        self._artist_resolvers = ArtistResolvers(self._artist_use_cases)
        self._music_resolvers = MusicResolvers(self._music_use_cases)

    @property
    def artist_repository(self) -> ArtistRepository:
        return self._artist_repository

    @property
    def music_repository(self) -> MusicRepository:
        return self._music_repository

    @property
    def artist_use_cases(self) -> ArtistUseCases:
        return self._artist_use_cases

    @property
    def music_use_cases(self) -> MusicUseCases:
        return self._music_use_cases

    @property
    def artist_resolvers(self) -> ArtistResolvers:
        return self._artist_resolvers

    @property
    def music_resolvers(self) -> MusicResolvers:
        return self._music_resolvers