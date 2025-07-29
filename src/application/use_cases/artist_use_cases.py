from dataclasses import dataclass
from typing import List, Optional
from src.domain.entities.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepository


@dataclass
class ArtistUseCases:
    """Casos de uso para artistas"""
    artist_repository: ArtistRepository

    def get_all_artists(self) -> List[Artist]:
        """Obtém todos os artistas"""
        return self.artist_repository.get_all()

    def get_artist_by_id(self, artist_id: int) -> Optional[Artist]:
        """Obtém um artista pelo ID"""
        return self.artist_repository.get_by_id(artist_id)

    def create_artist(self, name: str, status: bool = True) -> Artist:
        """Cria um novo artista"""
        artist = Artist(id=None, name=name, status=status)
        return self.artist_repository.create(artist)

    def update_artist(self, artist_id: int, name: str = None, status: bool = None) -> Optional[Artist]:
        """Atualiza um artista existente"""
        artist = self.artist_repository.get_by_id(artist_id)
        if not artist:
            return None

        if name is not None:
            artist.name = name
        if status is not None:
            artist.status = status

        return self.artist_repository.update(artist)

    def delete_artist(self, artist_id: int) -> bool:
        """Deleta um artista"""
        return self.artist_repository.delete(artist_id)

    def get_active_artists(self) -> List[Artist]:
        """Obtém apenas artistas ativos"""
        return self.artist_repository.get_active_artists()

    def deactivate_artist(self, artist_id: int) -> Optional[Artist]:
        """Desativa um artista"""
        artist = self.artist_repository.get_by_id(artist_id)
        if not artist:
            return None

        artist.deactivate()
        return self.artist_repository.update(artist)

    def activate_artist(self, artist_id: int) -> Optional[Artist]:
        """Ativa um artista"""
        artist = self.artist_repository.get_by_id(artist_id)
        if not artist:
            return None

        artist.activate()
        return self.artist_repository.update(artist)
