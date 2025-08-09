from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Artist:
    """Entidade de domínio para Artist"""

    id: Optional[int]
    name: str
    status: bool = True
    date: Optional[datetime] = None

    def __post_init__(self):
        if self.date is None:
            self.date = datetime.now()

    def is_active(self) -> bool:
        """Verifica se o artista está ativo"""
        return self.status

    def deactivate(self) -> None:
        """Desativa o artista"""
        self.status = False

    def activate(self) -> None:
        """Ativa o artista"""
        self.status = True
