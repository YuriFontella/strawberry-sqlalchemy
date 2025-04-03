import strawberry

from datetime import datetime


@strawberry.type
class Ouvidoria:
    uuid: str
    canal: str
    cpf: str
    atendimento: str
    motivo: str
    titulo: str
    descricao: str
    data: datetime


@strawberry.type
class Ludopatia:
    uuid: str
    email: str
    resultado: str
    criado: datetime
    atualizado: datetime
