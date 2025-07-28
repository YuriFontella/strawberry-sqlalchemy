from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.artist import Artist


class ArtistRepository(ABC):
    """Interface para o repositório de artistas"""
    
    @abstractmethod
    def get_all(self) -> List[Artist]:
        """Retorna todos os artistas"""
        pass
    
    @abstractmethod
    def get_by_id(self, artist_id: int) -> Optional[Artist]:
        """Retorna um artista pelo ID"""
        pass
    
    @abstractmethod
    def create(self, artist: Artist) -> Artist:
        """Cria um novo artista"""
        pass
    
    @abstractmethod
    def update(self, artist: Artist) -> Artist:
        """Atualiza um artista existente"""
        pass
    
    @abstractmethod
    def delete(self, artist_id: int) -> bool:
        """Deleta um artista pelo ID"""
        pass
    
    @abstractmethod
    def get_active_artists(self) -> List[Artist]:
        """Retorna apenas artistas ativos"""
        pass 