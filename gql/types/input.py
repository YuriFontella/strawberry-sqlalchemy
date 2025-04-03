import strawberry


@strawberry.input
class OuvidoriaInput:
    canal: str
    cpf: str
    atendimento: str
    motivo: str
    titulo: str
    descricao: str

@strawberry.input()
class LudopatiaInput:
    email: str
    resultado: str