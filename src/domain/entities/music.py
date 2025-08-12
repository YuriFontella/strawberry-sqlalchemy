from uuid import uuid4, UUID
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Music:
    """Entidade de domínio para Music"""

    title: str
    artist_uuid: UUID
    uuid: Optional[UUID] = field(default_factory=uuid4)
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

    def change_artist(self, new_artist_uuid: UUID) -> None:
        """Muda o artista da música"""
        self.artist_uuid = new_artist_uuid
        self.updated_at = datetime.now()
