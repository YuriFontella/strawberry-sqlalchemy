import strawberry


@strawberry.input
class ArtistInput:
    """Input GraphQL para Artist"""

    name: str
    status: bool = True


@strawberry.input
class ArtistUpdateInput:
    """Input GraphQL para atualização de Artist"""

    name: str
    status: bool
