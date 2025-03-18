from sqlalchemy import create_engine
from settings import URL

engine = create_engine(url=URL, echo=True)
