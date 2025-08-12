import strawberry
from src.domain.entities.music import Music


@strawberry.type
class MusicType(Music):
    """Tipo GraphQL para Music"""

    @classmethod
    def from_entity(cls, music: Music) -> "MusicType":
        """Converte entidade de domínio para tipo GraphQL"""
        return cls(uuid=music.uuid, title=music.title, artist_uuid=music.artist_uuid)
