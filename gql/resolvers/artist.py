from typing import List

from sqlalchemy import select, column, insert
from gql.types.input import ArtistInput

from orm.tables import artists
from orm.session import get_session

import gql.types.base as base


def get_artists() -> List["base.Artist"]:
    with get_session() as session:
        records = session.execute(select(artists))

    return [base.Artist(id=row.id, name=row.name) for row in records]


def post_artist(data: ArtistInput) -> "base.Artist":
    with get_session() as session:
        artist = insert(artists).values(name=data.name).returning(column('id'))
        result = session.execute(artist).scalar()

    return base.Artist(id=result, name=data.name)


def get_artist_by_id(artist_id) -> "base.Artist":
    with get_session() as session:
        record = session.execute(select(artists).where(column('id') == artist_id)).one()

    return base.Artist(id=record.id, name=record.name)
