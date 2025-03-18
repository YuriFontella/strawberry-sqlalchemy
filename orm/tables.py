from sqlalchemy import Table, MetaData, Column, String, Integer


metadata = MetaData()

artists = Table(
    'artists',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String)
)

musics = Table(
    'musics',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String),
    Column('artist_id', Integer)
)
