from dataclasses import dataclass
from strawberry.fastapi import BaseContext
from src.presentation.graphql.artist.resolver import ArtistResolvers
from src.presentation.graphql.music.resolver import MusicResolvers


@dataclass
class GraphQLContext(BaseContext):
    """Contexto do GraphQL com as dependências injetadas"""
    artist_resolvers: ArtistResolvers
    music_resolvers: MusicResolvers
