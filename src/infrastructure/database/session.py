from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import metadata
from src.infrastructure.config.settings import get_database_url

# Criar engine do banco de dados
engine = create_engine(get_database_url())

# Criar session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session():
    """Context manager para obter uma sessão do banco de dados"""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_tables():
    """Cria todas as tabelas no banco de dados"""
    metadata.create_all(bind=engine) 