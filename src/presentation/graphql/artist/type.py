import strawberry
from src.domain.entities.artist import Artist


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
