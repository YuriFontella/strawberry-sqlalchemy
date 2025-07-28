from typing import List, Optional
from src.domain.entities.music import Music
from src.domain.repositories.music_repository import MusicRepository


class MusicUseCases:
    """Casos de uso para músicas"""

    def __init__(self, music_repository: MusicRepository):
        self.music_repository = music_repository

    def get_all_musics(self) -> List[Music]:
        """Obtém todas as músicas"""
        return self.music_repository.get_all()
    
    def get_music_by_id(self, music_id: int) -> Optional[Music]:
        """Obtém uma música pelo ID"""
        return self.music_repository.get_by_id(music_id)
    
    def get_musics_by_artist(self, artist_id: int) -> List[Music]:
        """Obtém todas as músicas de um artista"""
        return self.music_repository.get_by_artist_id(artist_id)
    
    def create_music(self, title: str, artist_id: int) -> Music:
        """Cria uma nova música"""
        music = Music(id=None, title=title, artist_id=artist_id)
        return self.music_repository.create(music)
    
    def update_music(self, music_id: int, title: str = None, artist_id: int = None) -> Optional[Music]:
        """Atualiza uma música existente"""
        music = self.music_repository.get_by_id(music_id)
        if not music:
            return None
        
        if title is not None:
            music.update_title(title)
        if artist_id is not None:
            music.change_artist(artist_id)
        
        return self.music_repository.update(music)
    
    def delete_music(self, music_id: int) -> bool:
        """Deleta uma música"""
        return self.music_repository.delete(music_id)
    
    def update_music_title(self, music_id: int, new_title: str) -> Optional[Music]:
        """Atualiza apenas o título de uma música"""
        music = self.music_repository.get_by_id(music_id)
        if not music:
            return None
        
        music.update_title(new_title)
        return self.music_repository.update(music)
    
    def change_music_artist(self, music_id: int, new_artist_id: int) -> Optional[Music]:
        """Muda o artista de uma música"""
        music = self.music_repository.get_by_id(music_id)
        if not music:
            return None
        
        music.change_artist(new_artist_id)
        return self.music_repository.update(music) 