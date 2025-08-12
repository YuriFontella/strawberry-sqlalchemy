import strawberry

from src.domain.entities.artist import Artist


@strawberry.input
class ArtistInput(Artist):
    """Input GraphQL para Artist"""


@strawberry.input
class ArtistUpdateInput(Artist):
    """Input GraphQL para atualização de Artist"""
