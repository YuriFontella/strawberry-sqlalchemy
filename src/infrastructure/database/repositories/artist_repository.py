from typing import List, Optional
from sqlalchemy import select, insert, update, delete, column
from src.domain.entities.artist import Artist
from src.domain.repositories.artist_repository import ArtistRepository
from src.infrastructure.database.models import artists
from src.infrastructure.database.session import get_session


class SQLAlchemyArtistRepository(ArtistRepository):
    """Implementação do repositório de artistas usando SQLAlchemy"""

    def get_all(self) -> List[Artist]:
        with get_session() as session:
            records = session.execute(select(artists))
            return [
                Artist(uuid=row.uuid, name=row.name, status=row.status, date=row.date)
                for row in records
            ]

    def get_by_id(self, artist_uuid: int) -> Optional[Artist]:
        with get_session() as session:
            record = session.execute(
                select(artists).where(artists.c.uuid == artist_uuid)
            ).first()

            if not record:
                return None

            return Artist(
                uuid=record.uuid,
                name=record.name,
                status=record.status,
                date=record.date,
            )

    def create(self, artist: Artist) -> Artist:
        with get_session() as session:
            result = session.execute(
                insert(artists)
                .values(uuid=artist.uuid, name=artist.name, status=artist.status)
                .returning(column("uuid"))
            ).scalar()

            return Artist(
                uuid=result, name=artist.name, status=artist.status, date=artist.date
            )

    def update(self, artist: Artist) -> Artist:
        with get_session() as session:
            session.execute(
                update(artists)
                .where(artists.c.uuid == artist.uuid)
                .values(name=artist.name, status=artist.status)
            )

            return artist

    def delete(self, artist_uuid: int) -> bool:
        with get_session() as session:
            result = session.execute(
                delete(artists).where(artists.c.uuid == artist_uuid)
            )
            return result.rowcount > 0

    def get_active_artists(self) -> List[Artist]:
        with get_session() as session:
            records = session.execute(select(artists).where(artists.c.status == True))
            return [
                Artist(uuid=row.uuid, name=row.name, status=row.status, date=row.date)
                for row in records
            ]
