from sqlalchemy import create_engine
from settings import DSN

engine = create_engine(DSN)
