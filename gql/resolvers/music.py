import typing

import gql.types.base as base

from sqlalchemy import select, column, insert
from gql.types.input import MusicInput

from orm.tables import musics
from orm.session import get_session


def get_musics() -> typing.List["base.Music"]:
    with get_session() as session:
        records = session.execute(select(musics))

    return [base.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]


def post_music(data: MusicInput) -> "base.Music":
    with get_session() as session:
        music = insert(musics).values(title=data.title, artist_id=data.artist_id).returning(column('id'), column('artist_id'))
        result = session.execute(music).one()

    return base.Music(id=result.id, title=data.title, artist_id=result.artist_id)


def get_musics_by_artist(artist_id) -> typing.List["base.Music"]:
    with get_session() as session:
        records = session.execute(select(musics).where(column('artist_id') == artist_id))

    return [base.Music(id=row.id, title=row.title, artist_id=row.artist_id) for row in records]
