from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from src.application.use_cases.artist_use_cases import ArtistUseCases
from src.presentation.graphql.artist.type import ArtistType
from src.presentation.graphql.artist.input import ArtistInput, ArtistUpdateInput


@dataclass
class ArtistResolvers:
    """Resolvers para Artist"""

    artist_use_cases: ArtistUseCases

    def get_artists(self) -> List[ArtistType]:
        """Obtém todos os artistas"""
        artists = self.artist_use_cases.get_all_artists()
        return [ArtistType.from_entity(artist) for artist in artists]

    def get_artist_by_id(self, artist_uuid: UUID) -> Optional[ArtistType]:
        """Obtém um artista pelo UUID"""
        artist = self.artist_use_cases.get_artist_by_id(artist_uuid)
        return ArtistType.from_entity(artist) if artist else None

    def create_artist(self, data: ArtistInput) -> ArtistType:
        """Cria um novo artista"""
        artist = self.artist_use_cases.create_artist(data.name, data.status)
        return ArtistType.from_entity(artist)

    def update_artist(
        self, artist_uuid: UUID, data: ArtistUpdateInput
    ) -> Optional[ArtistType]:
        """Atualiza um artista"""
        artist = self.artist_use_cases.update_artist(
            artist_uuid, name=data.name, status=data.status
        )
        return ArtistType.from_entity(artist) if artist else None

    def delete_artist(self, artist_uuid: UUID) -> bool:
        """Deleta um artista"""
        return self.artist_use_cases.delete_artist(artist_uuid)

    def get_active_artists(self) -> List[ArtistType]:
        """Obtém apenas artistas ativos"""
        artists = self.artist_use_cases.get_active_artists()
        return [ArtistType.from_entity(artist) for artist in artists]
