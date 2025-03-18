import typing

import gql.types.model as model

from sqlalchemy import select, column

from orm.tables import musics
from orm.session import get_session


def get_musics() -> typing.List["model.Music"]:
    with get_session() as session:
        records = session.execute(select(musics))

    return [model.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]


def get_musics_by_artist(artist_id) -> typing.List["model.Music"]:
    with get_session() as session:
        records = session.execute(select(musics).where(column('artist_id') == artist_id))

    return [model.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]
