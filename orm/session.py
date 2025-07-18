import logging

from typing import Generator
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from orm.engine import engine

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        logging.exception("Erro durante a transação com o banco de dados")
        raise
    finally:
        session.close()
