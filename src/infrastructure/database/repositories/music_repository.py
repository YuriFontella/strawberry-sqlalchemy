from typing import List, Optional
from sqlalchemy import select, insert, update, delete, column
from src.domain.entities.music import Music
from src.domain.repositories.music_repository import MusicRepository
from ..models import musics
from ..session import get_session


class SQLAlchemyMusicRepository(MusicRepository):
    """Implementação do repositório de músicas usando SQLAlchemy"""

    def get_all(self) -> List[Music]:
        with get_session() as session:
            records = session.execute(select(musics))
            return [
                Music(
                    id=row.id,
                    title=row.title,
                    artist_id=row.artist_id,
                    created_at=row.created_at,
                    updated_at=row.updated_at
                ) for row in records
            ]

    def get_by_id(self, music_id: int) -> Optional[Music]:
        with get_session() as session:
            record = session.execute(
                select(musics).where(musics.c.id == music_id)
            ).first()

            if not record:
                return None

            return Music(
                id=record.id,
                title=record.title,
                artist_id=record.artist_id,
                created_at=record.created_at,
                updated_at=record.updated_at
            )

    def get_by_artist_id(self, artist_id: int) -> List[Music]:
        with get_session() as session:
            records = session.execute(
                select(musics).where(musics.c.artist_id == artist_id)
            )
            return [
                Music(
                    id=row.id,
                    title=row.title,
                    artist_id=row.artist_id,
                    created_at=row.created_at,
                    updated_at=row.updated_at
                ) for row in records
            ]

    def create(self, music: Music) -> Music:
        with get_session() as session:
            result = session.execute(
                insert(musics).values(
                    title=music.title,
                    artist_id=music.artist_id
                ).returning(column('id'))
            ).scalar()

            return Music(
                id=result,
                title=music.title,
                artist_id=music.artist_id,
                created_at=music.created_at,
                updated_at=music.updated_at
            )

    def update(self, music: Music) -> Music:
        with get_session() as session:
            session.execute(
                update(musics)
                .where(musics.c.id == music.id)
                .values(
                    title=music.title,
                    artist_id=music.artist_id,
                    updated_at=music.updated_at
                )
            )

            return music

    def delete(self, music_id: int) -> bool:
        with get_session() as session:
            result = session.execute(
                delete(musics).where(musics.c.id == music_id)
            )
            return result.rowcount > 0