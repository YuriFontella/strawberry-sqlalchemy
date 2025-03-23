import strawberry

from typing import List

from gql.resolvers.music import get_musics_by_artist
from gql.resolvers.artist import get_artist_by_id


@strawberry.type
class Artist:
    id: int
    name: str

    @strawberry.field()
    def musics(self) -> List["Music"]:
        return get_musics_by_artist(self.id)


@strawberry.type
class Music:
    id: int
    title: str
    artist_id: int

    @strawberry.field()
    def artist(self) -> "Artist":
        return get_artist_by_id(self.artist_id)
