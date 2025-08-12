import strawberry
from strawberry.tools import merge_types

from strawberry.schema.config import StrawberryConfig
from src.presentation.graphql.artist.schema import (
    ArtistQuery,
    ArtistMutation,
    ArtistSubscription,
)
from src.presentation.graphql.music.schema import (
    MusicQuery,
    MusicMutation,
    MusicSubscription,
)

# Combine os tipos usando merge_types
Query = merge_types("Query", (ArtistQuery, MusicQuery))
Mutation = merge_types("Mutation", (ArtistMutation, MusicMutation))
Subscription = merge_types("Subscription", (ArtistSubscription, MusicSubscription))


def create_schema() -> strawberry.Schema:
    """Cria o schema GraphQL federado"""
    return strawberry.Schema(
        query=Query,
        mutation=Mutation,
        subscription=Subscription,
        config=StrawberryConfig(auto_camel_case=False),
    )
