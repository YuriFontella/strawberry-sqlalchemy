import strawberry


def hello():
    return True

@strawberry.type
class RootQuery:
    hello: bool = strawberry.field(resolver=hello)
