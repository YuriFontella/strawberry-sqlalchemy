from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from src.application.use_cases.music_use_cases import MusicUseCases
from src.presentation.graphql.music.type import MusicType
from src.presentation.graphql.music.input import MusicInput, MusicUpdateInput


@dataclass
class MusicResolvers:
    """Resolvers para Music"""

    music_use_cases: MusicUseCases

    def get_musics(self) -> List[MusicType]:
        """Obtém todas as músicas"""
        musics = self.music_use_cases.get_all_musics()
        return [MusicType.from_entity(music) for music in musics]

    def get_music_by_id(self, music_uuid: UUID) -> Optional[MusicType]:
        """Obtém uma música pelo UUID"""
        music = self.music_use_cases.get_music_by_id(music_uuid)
        return MusicType.from_entity(music) if music else None

    def get_musics_by_artist(self, artist_uuid: UUID) -> List[MusicType]:
        """Obtém todas as músicas de um artista"""
        musics = self.music_use_cases.get_musics_by_artist(artist_uuid)
        return [MusicType.from_entity(music) for music in musics]

    def create_music(self, data: MusicInput) -> MusicType:
        """Cria uma nova música"""
        music = self.music_use_cases.create_music(data.title, data.artist_uuid)
        return MusicType.from_entity(music)

    def update_music(
        self, music_uuid: UUID, data: MusicUpdateInput
    ) -> Optional[MusicType]:
        """Atualiza uma música"""
        music = self.music_use_cases.update_music(
            music_uuid, title=data.title, artist_uuid=data.artist_uuid
        )
        return MusicType.from_entity(music) if music else None

    def delete_music(self, music_uuid: UUID) -> bool:
        """Deleta uma música"""
        return self.music_use_cases.delete_music(music_uuid)
