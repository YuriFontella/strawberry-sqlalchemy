import strawberry

from typing import List

from gql.types.base import Artist
from gql.resolvers.artist import get_artists, post_artist


@strawberry.type
class ArtistQuery:
    artists: List[Artist] = strawberry.field(resolver=get_artists)


@strawberry.type
class ArtistMutation:
    add_artist: Artist = strawberry.field(resolver=post_artist)
