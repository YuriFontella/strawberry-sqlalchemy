import typing

import gql.types.model as model

from sqlalchemy import select, column, insert
from gql.types.input import ArtistInput

from orm.tables import artists
from orm.session import get_session


def get_artists() -> typing.List["model.Artist"]:
    with get_session() as session:
        records = session.execute(select(artists))

    return [model.Artist(id=row.id, name=row.name) for row in records]


def post_artist(data: ArtistInput) -> "model.Artist":
    with get_session() as session:
        artist = insert(artists).values(name=data.name).returning(column('id'))
        result = session.execute(artist).scalar()

    return model.Artist(id=result, name=data.name)


def get_artist_by_id(artist_id) -> "model.Artist":
    with get_session() as session:
        record = session.execute(select(artists).where(column('id') == artist_id)).one()

    return model.Artist(id=record.id, name=record.name)
