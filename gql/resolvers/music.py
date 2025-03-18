import typing

import gql.types.model as model

from sqlalchemy.orm import Session
from sqlalchemy import select, column

from orm.tables import musics
from orm.engine import engine


def get_musics() -> typing.List["model.Music"]:
    with Session(engine) as session:
        records = session.execute(select(musics))

    return [model.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]


def get_musics_by_artist(artist_id) -> typing.List["model.Music"]:
    with Session(engine) as session:
        records = session.execute(select(musics).where(column('artist_id') == artist_id))

    return [model.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]
