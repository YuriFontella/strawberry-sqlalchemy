import strawberry


@strawberry.input
class MusicInput:
    """Input GraphQL para Music"""
    title: str
    artist_id: int


@strawberry.input
class MusicUpdateInput:
    """Input GraphQL para atualização de Music"""
    title: str
    artist_id: int
