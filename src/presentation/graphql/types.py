import strawberry
from src.domain.entities.artist import Artist
from src.domain.entities.music import Music


@strawberry.type
class ArtistType:
    """Tipo GraphQL para Artist"""
    id: int | None
    name: str
    status: bool
    
    @classmethod
    def from_entity(cls, artist: Artist) -> 'ArtistType':
        """Converte entidade de domínio para tipo GraphQL"""
        return cls(
            id=artist.id,
            name=artist.name,
            status=artist.status
        )


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