from typing import List, Optional
from sqlalchemy import select, insert, update, delete, column
from src.domain.entities.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepository
from ..models import artists
from ..session import get_session


class SQLAlchemyArtistRepository(ArtistRepository):
    """Implementação do repositório de artistas usando SQLAlchemy"""

    def get_all(self) -> List[Artist]:
        with get_session() as session:
            records = session.execute(select(artists))
            return [
                Artist(
                    id=row.id,
                    name=row.name,
                    status=row.status,
                    date=row.date
                ) for row in records
            ]

    def get_by_id(self, artist_id: int) -> Optional[Artist]:
        with get_session() as session:
            record = session.execute(
                select(artists).where(artists.c.id == artist_id)
            ).first()

            if not record:
                return None

            return Artist(
                id=record.id,
                name=record.name,
                status=record.status,
                date=record.date
            )

    def create(self, artist: Artist) -> Artist:
        with get_session() as session:
            result = session.execute(
                insert(artists).values(
                    name=artist.name,
                    status=artist.status
                ).returning(column('id'))
            ).scalar()

            return Artist(
                id=result,
                name=artist.name,
                status=artist.status,
                date=artist.date
            )

    def update(self, artist: Artist) -> Artist:
        with get_session() as session:
            session.execute(
                update(artists)
                .where(artists.c.id == artist.id)
                .values(
                    name=artist.name,
                    status=artist.status
                )
            )

            return artist

    def delete(self, artist_id: int) -> bool:
        with get_session() as session:
            result = session.execute(
                delete(artists).where(artists.c.id == artist_id)
            )
            return result.rowcount > 0

    def get_active_artists(self) -> List[Artist]:
        with get_session() as session:
            records = session.execute(
                select(artists).where(artists.c.status == True)
            )
            return [
                Artist(
                    id=row.id,
                    name=row.name,
                    status=row.status,
                    date=row.date
                ) for row in records
            ]