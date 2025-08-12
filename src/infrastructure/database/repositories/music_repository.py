from typing import List, Optional
from sqlalchemy import select, insert, update, delete, column
from src.domain.entities.music import Music
from src.domain.repositories.music_repository import MusicRepository
from src.infrastructure.database.models import musics
from src.infrastructure.database.session import get_session


class SQLAlchemyMusicRepository(MusicRepository):
    """Implementação do repositório de músicas usando SQLAlchemy"""

    def get_all(self) -> List[Music]:
        with get_session() as session:
            records = session.execute(select(musics))
            return [
                Music(
                    uuid=row.uuid,
                    title=row.title,
                    artist_uuid=row.artist_uuid,
                    created_at=row.created_at,
                    updated_at=row.updated_at,
                )
                for row in records
            ]

    def get_by_id(self, music_uuid: int) -> Optional[Music]:
        with get_session() as session:
            record = session.execute(
                select(musics).where(musics.c.uuid == music_uuid)
            ).first()

            if not record:
                return None

            return Music(
                uuid=record.uuid,
                title=record.title,
                artist_uuid=record.artist_uuid,
                created_at=record.created_at,
                updated_at=record.updated_at,
            )

    def get_by_artist_uuid(self, artist_uuid: int) -> List[Music]:
        with get_session() as session:
            records = session.execute(
                select(musics).where(musics.c.artist_uuid == artist_uuid)
            )
            return [
                Music(
                    uuid=row.uuid,
                    title=row.title,
                    artist_uuid=row.artist_uuid,
                    created_at=row.created_at,
                    updated_at=row.updated_at,
                )
                for row in records
            ]

    def create(self, music: Music) -> Music:
        with get_session() as session:
            result = session.execute(
                insert(musics)
                .values(
                    uuid=music.uuid, title=music.title, artist_uuid=music.artist_uuid
                )
                .returning(column("uuid"))
            ).scalar()

            return Music(
                uuid=result,
                title=music.title,
                artist_uuid=music.artist_uuid,
                created_at=music.created_at,
                updated_at=music.updated_at,
            )

    def update(self, music: Music) -> Music:
        with get_session() as session:
            session.execute(
                update(musics)
                .where(musics.c.uuid == music.uuid)
                .values(
                    title=music.title,
                    artist_uuid=music.artist_uuid,
                    updated_at=music.updated_at,
                )
            )

            return music

    def delete(self, music_uuid: int) -> bool:
        with get_session() as session:
            result = session.execute(delete(musics).where(musics.c.uuid == music_uuid))
            return result.rowcount > 0
