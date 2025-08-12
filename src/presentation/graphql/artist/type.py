import strawberry
from src.domain.entities.artist import Artist


@strawberry.type
class ArtistType(Artist):
    """Tipo GraphQL para Artist"""

    @classmethod
    def from_entity(cls, artist: Artist) -> "ArtistType":
        """Converte entidade de domínio para tipo GraphQL"""
        return cls(uuid=artist.uuid, name=artist.name, status=artist.status)
