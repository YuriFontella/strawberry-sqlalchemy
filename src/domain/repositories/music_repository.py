from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.music import Music


class MusicRepository(ABC):
    """Interface para o repositório de músicas"""
    
    @abstractmethod
    def get_all(self) -> List[Music]:
        """Retorna todas as músicas"""
        pass
    
    @abstractmethod
    def get_by_id(self, music_id: int) -> Optional[Music]:
        """Retorna uma música pelo ID"""
        pass
    
    @abstractmethod
    def get_by_artist_id(self, artist_id: int) -> List[Music]:
        """Retorna todas as músicas de um artista"""
        pass
    
    @abstractmethod
    def create(self, music: Music) -> Music:
        """Cria uma nova música"""
        pass
    
    @abstractmethod
    def update(self, music: Music) -> Music:
        """Atualiza uma música existente"""
        pass
    
    @abstractmethod
    def delete(self, music_id: int) -> bool:
        """Deleta uma música pelo ID"""
        pass 