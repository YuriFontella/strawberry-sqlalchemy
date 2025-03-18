import strawberry


@strawberry.input
class ArtistInput:
    name: str


@strawberry.input
class MusicInput:
    title: str
    artist_id: int
