from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from settings import URL

engine = create_engine(
    url=URL,
    echo=False,
    poolclass=QueuePool,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=30,
    pool_size=2,
    max_overflow=8
)
