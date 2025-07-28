from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Music:
    """Entidade de domínio para Music"""
    id: Optional[int]
    title: str
    artist_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def update_title(self, new_title: str) -> None:
        """Atualiza o título da música"""
        self.title = new_title
        self.updated_at = datetime.now()
    
    def change_artist(self, new_artist_id: int) -> None:
        """Muda o artista da música"""
        self.artist_id = new_artist_id
        self.updated_at = datetime.now() 