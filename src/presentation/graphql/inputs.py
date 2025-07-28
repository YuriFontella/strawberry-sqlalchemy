import strawberry


@strawberry.input
class ArtistInput:
    """Input GraphQL para Artist"""
    name: str
    status: bool = True


@strawberry.input
class MusicInput:
    """Input GraphQL para Music"""
    title: str
    artist_id: int


@strawberry.input
class ArtistUpdateInput:
    """Input GraphQL para atualização de Artist"""
    name: str | None = None
    status: bool | None = None


@strawberry.input
class MusicUpdateInput:
    """Input GraphQL para atualização de Music"""
    title: str | None = None
    artist_id: int | None = None 