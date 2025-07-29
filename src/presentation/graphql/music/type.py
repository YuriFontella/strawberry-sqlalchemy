import strawberry
from src.domain.entities.music import Music


@strawberry.type
class MusicType:
    """Tipo GraphQL para Music"""
    id: int | None
    title: str
    artist_id: int = strawberry.field(name="artist_id")

    @classmethod
    def from_entity(cls, music: Music) -> 'MusicType':
        """Converte entidade de domínio para tipo GraphQL"""
        return cls(
            id=music.id,
            title=music.title,
            artist_id=music.artist_id
        )
