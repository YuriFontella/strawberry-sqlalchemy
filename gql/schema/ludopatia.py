import strawberry

from gql.resolvers.ludopatia import post_ludopatia


@strawberry.type
class LudopatiaMutation:
    add_ludopatia: bool = strawberry.field(resolver=post_ludopatia)
