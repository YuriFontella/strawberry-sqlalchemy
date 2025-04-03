from sqlalchemy import insert

from orm.tables import ludopatia
from orm.session import get_session

from gql.types.input import LudopatiaInput


def post_ludopatia(data: LudopatiaInput) -> bool:
    with get_session() as session:
        query = insert(ludopatia).values(data.__dict__)
        session.execute(query)

    return True
