from sqlalchemy import Table, MetaData, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.sql import func

metadata = MetaData()

artists = Table(
    'artists',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, unique=True, nullable=False, index=True),
    Column('date', DateTime, default=func.now())
)

musics = Table(
    'musics',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False, index=True),
    Column('artist_id', Integer, ForeignKey('artists.id'), nullable=False),
    Column('created_at', DateTime, default=func.now()),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
)
