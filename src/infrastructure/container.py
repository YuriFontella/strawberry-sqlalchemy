from dataclasses import dataclass, field
from functools import cached_property
from src.domain.repositories.artist_repository import ArtistRepository
from src.domain.repositories.music_repository import MusicRepository
from src.application.use_cases.artist_use_cases import ArtistUseCases
from src.application.use_cases.music_use_cases import MusicUseCases
from src.presentation.graphql.artist.resolver import ArtistResolvers
from src.presentation.graphql.music.resolver import MusicResolvers
from src.infrastructure.database.repositories.artist_repository import SQLAlchemyArtistRepository
from src.infrastructure.database.repositories.music_repository import SQLAlchemyMusicRepository


@dataclass
class Container:
    """Container de injeção de dependências"""

    # Permite injetar repositórios personalizados para testes
    artist_repository: ArtistRepository = field(default_factory=SQLAlchemyArtistRepository)
    music_repository: MusicRepository = field(default_factory=SQLAlchemyMusicRepository)

    @cached_property
    def artist_use_cases(self) -> ArtistUseCases:
        return ArtistUseCases(self.artist_repository)

    @cached_property
    def music_use_cases(self) -> MusicUseCases:
        return MusicUseCases(self.music_repository)

    @cached_property
    def artist_resolvers(self) -> ArtistResolvers:
        return ArtistResolvers(self.artist_use_cases)

    @cached_property
    def music_resolvers(self) -> MusicResolvers:
        return MusicResolvers(self.music_use_cases)
