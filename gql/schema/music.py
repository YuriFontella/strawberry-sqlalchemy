import typing
import strawberry

from gql.types.model import Music
from gql.resolvers.music import get_musics, post_music


@strawberry.type
class MusicQuery:
    musics: typing.List[Music] = strawberry.field(resolver=get_musics)


@strawberry.type
class MusicMutation:
    add_music: Music = strawberry.field(resolver=post_music)
