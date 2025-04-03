from sqlalchemy import insert

from orm.tables import ouvidoria
from orm.session import get_session

from gql.types.input import OuvidoriaInput


def post_ouvidoria(data: OuvidoriaInput) -> bool:
    with get_session() as session:
        query = insert(ouvidoria).values(data.__dict__)
        session.execute(query)

    return True
