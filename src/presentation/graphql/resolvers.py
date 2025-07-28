from typing import List, Optional
from src.application.use_cases.music_use_cases import MusicUseCases
from .types import ArtistType, MusicType
from .inputs import ArtistInput, MusicInput, ArtistUpdateInput, MusicUpdateInput


class ArtistResolvers:
    """Resolvers para Artist"""

    def __init__(self, artist_use_cases):
        self.artist_use_cases = artist_use_cases

    def get_artists(self) -> List[ArtistType]:
        """Obtém todos os artistas"""
        artists = self.artist_use_cases.get_all_artists()
        return [ArtistType.from_entity(artist) for artist in artists]

    def get_artist_by_id(self, artist_id: int) -> Optional[ArtistType]:
        """Obtém um artista pelo ID"""
        artist = self.artist_use_cases.get_artist_by_id(artist_id)
        return ArtistType.from_entity(artist) if artist else None

    def create_artist(self, data: ArtistInput) -> ArtistType:
        """Cria um novo artista"""
        artist = self.artist_use_cases.create_artist(data.name, data.status)
        return ArtistType.from_entity(artist)

    def update_artist(self, artist_id: int, data: ArtistUpdateInput) -> Optional[ArtistType]:
        """Atualiza um artista"""
        artist = self.artist_use_cases.update_artist(
            artist_id, 
            name=data.name, 
            status=data.status
        )
        return ArtistType.from_entity(artist) if artist else None

    def delete_artist(self, artist_id: int) -> bool:
        """Deleta um artista"""
        return self.artist_use_cases.delete_artist(artist_id)

    def get_active_artists(self) -> List[ArtistType]:
        """Obtém apenas artistas ativos"""
        artists = self.artist_use_cases.get_active_artists()
        return [ArtistType.from_entity(artist) for artist in artists]


class MusicResolvers:
    """Resolvers para Music"""
    def __init__(self, music_use_cases):
        self.music_use_cases = music_use_cases

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