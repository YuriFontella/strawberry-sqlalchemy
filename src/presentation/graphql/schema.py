import strawberry
from .artist.schema import ArtistQuery, ArtistMutation, ArtistSubscription
from .music.schema import MusicQuery, MusicMutation, MusicSubscription


@strawberry.type
class Query(ArtistQuery, MusicQuery):
    """Query principal que herda de todos os módulos"""

    pass


@strawberry.type
class Mutation(ArtistMutation, MusicMutation):
    """Mutation principal que herda de todos os módulos"""

    pass


@strawberry.type
class Subscription(ArtistSubscription, MusicSubscription):
    """Subscription principal que herda de todos os módulos"""

    pass


def create_schema() -> strawberry.Schema:
    """Cria o schema GraphQL federado"""
    return strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
