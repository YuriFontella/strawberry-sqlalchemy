import typing
import strawberry

from gql.types.model import Music
from gql.resolvers.music import get_musics


@strawberry.type
class MusicQuery:
    musics: typing.List[Music] = strawberry.field(resolver=get_musics)
