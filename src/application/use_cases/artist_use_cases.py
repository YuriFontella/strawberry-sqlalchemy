from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from src.domain.entities.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepository
from src.infrastructure.config.log import get_logger


@dataclass
class ArtistUseCases:
    """Casos de uso para artistas"""

    artist_repository: ArtistRepository

    def __post_init__(self):
        self.logger = get_logger(__name__)

    def get_all_artists(self) -> List[Artist]:
        """Obtém todos os artistas"""
        self.logger.info("Buscando todos os artistas")
        return self.artist_repository.get_all()

    def get_artist_by_id(self, artist_uuid: UUID) -> Optional[Artist]:
        """Obtém um artista pelo UUID"""
        self.logger.info("Buscando artista", id=str(artist_uuid))
        return self.artist_repository.get_by_id(artist_uuid)

    def create_artist(self, name: str, status: bool = True) -> Artist:
        """Cria um novo artista"""
        self.logger.info("Criando artista", name=name)
        artist = Artist(name=name, status=status)
        return self.artist_repository.create(artist)

    def update_artist(
        self, artist_uuid: UUID, name: str = None, status: bool = None
    ) -> Optional[Artist]:
        """Atualiza um artista existente"""
        self.logger.info("Atualizando artista", id=str(artist_uuid))

        artist = self.artist_repository.get_by_id(artist_uuid)
        if not artist:
            return None

        if name is not None:
            artist.name = name
        if status is not None:
            artist.status = status

        return self.artist_repository.update(artist)

    def delete_artist(self, artist_uuid: UUID) -> bool:
        """Deleta um artista"""
        self.logger.info("Deletando artista", id=str(artist_uuid))
        return self.artist_repository.delete(artist_uuid)

    def get_active_artists(self) -> List[Artist]:
        """Obtém apenas artistas ativos"""
        return self.artist_repository.get_active_artists()

    def deactivate_artist(self, artist_uuid: UUID) -> Optional[Artist]:
        """Desativa um artista"""
        artist = self.artist_repository.get_by_id(artist_uuid)
        if not artist:
            return None

        artist.deactivate()
        return self.artist_repository.update(artist)

    def activate_artist(self, artist_uuid: UUID) -> Optional[Artist]:
        """Ativa um artista"""
        artist = self.artist_repository.get_by_id(artist_uuid)
        if not artist:
            return None

        artist.activate()
        return self.artist_repository.update(artist)
