from orm.engine import engine
from orm.tables import metadata


def create_all():
    return metadata.create_all(engine)
