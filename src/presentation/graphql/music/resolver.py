from dataclasses import dataclass
from typing import List, Optional
from src.application.use_cases.music_use_cases import MusicUseCases
from .type import MusicType
from .input import MusicInput, MusicUpdateInput


@dataclass
class MusicResolvers:
    """Resolvers para Music"""
    music_use_cases: MusicUseCases

    def get_musics(self) -> List[MusicType]:
        """Obtém todas as músicas"""
        musics = self.music_use_cases.get_all_musics()
        return [MusicType.from_entity(music) for music in musics]

    def get_music_by_id(self, music_id: int) -> Optional[MusicType]:
        """Obtém uma música pelo ID"""
        music = self.music_use_cases.get_music_by_id(music_id)
        return MusicType.from_entity(music) if music else None

    def get_musics_by_artist(self, artist_id: int) -> List[MusicType]:
        """Obtém todas as músicas de um artista"""
        musics = self.music_use_cases.get_musics_by_artist(artist_id)
        return [MusicType.from_entity(music) for music in musics]

    def create_music(self, data: MusicInput) -> MusicType:
        """Cria uma nova música"""
        music = self.music_use_cases.create_music(data.title, data.artist_id)
        return MusicType.from_entity(music)

    def update_music(self, music_id: int, data: MusicUpdateInput) -> Optional[MusicType]:
        """Atualiza uma música"""
        music = self.music_use_cases.update_music(
            music_id,
            title=data.title,
            artist_id=data.artist_id
        )
        return MusicType.from_entity(music) if music else None

    def delete_music(self, music_id: int) -> bool:
        """Deleta uma música"""
        return self.music_use_cases.delete_music(music_id)
