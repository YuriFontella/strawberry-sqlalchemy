import strawberry


@strawberry.type
class RootQuery:
    @strawberry.field
    def hello(self) -> str:
        return 'Hello'
