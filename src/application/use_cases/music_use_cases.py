from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from src.domain.entities.music import Music
from src.domain.repositories.music_repository import MusicRepository


@dataclass
class MusicUseCases:
    """Casos de uso para músicas"""

    music_repository: MusicRepository

    def get_all_musics(self) -> List[Music]:
        """Obtém todas as músicas"""
        return self.music_repository.get_all()

    def get_music_by_id(self, music_uuid: UUID) -> Optional[Music]:
        """Obtém uma música pelo UUID"""
        return self.music_repository.get_by_id(music_uuid)

    def get_musics_by_artist(self, artist_uuid: UUID) -> List[Music]:
        """Obtém todas as músicas de um artista"""
        return self.music_repository.get_by_artist_uuid(artist_uuid)

    def create_music(self, title: str, artist_uuid: UUID) -> Music:
        """Cria uma nova música"""
        music = Music(title=title, artist_uuid=artist_uuid)
        return self.music_repository.create(music)

    def update_music(
        self, music_uuid: UUID, title: str = None, artist_uuid: UUID = None
    ) -> Optional[Music]:
        """Atualiza uma música existente"""
        music = self.music_repository.get_by_id(music_uuid)
        if not music:
            return None

        if title is not None:
            music.update_title(title)
        if artist_uuid is not None:
            music.change_artist(artist_uuid)

        return self.music_repository.update(music)

    def delete_music(self, music_uuid: UUID) -> bool:
        """Deleta uma música"""
        return self.music_repository.delete(music_uuid)

    def update_music_title(self, music_uuid: UUID, new_title: str) -> Optional[Music]:
        """Atualiza apenas o título de uma música"""
        music = self.music_repository.get_by_id(music_uuid)
        if not music:
            return None

        music.update_title(new_title)
        return self.music_repository.update(music)

    def change_music_artist(
        self, music_uuid: UUID, new_artist_uuid: UUID
    ) -> Optional[Music]:
        """Muda o artista de uma música"""
        music = self.music_repository.get_by_id(music_uuid)
        if not music:
            return None

        music.change_artist(new_artist_uuid)
        return self.music_repository.update(music)
