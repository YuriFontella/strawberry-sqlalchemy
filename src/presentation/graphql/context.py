from dataclasses import dataclass
from strawberry.fastapi import BaseContext
from src.presentation.graphql.resolvers import ArtistResolvers, MusicResolvers

@dataclass
class GraphQLContext(BaseContext):
    """Contexto do GraphQL com as dependências injetadas"""
    artist_resolvers: ArtistResolvers
    music_resolvers: MusicResolvers
