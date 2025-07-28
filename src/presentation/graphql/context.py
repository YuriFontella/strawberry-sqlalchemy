from dataclasses import dataclass
from strawberry.fastapi import BaseContext
from src.presentation.graphql.resolvers import ArtistResolvers, MusicResolvers

@dataclass
class GraphQLContext(BaseContext):
    """Contexto do GraphQL com as dependências injetadas"""
    artist_resolvers: ArtistResolvers
    music_resolvers: MusicResolvers

    def __post_init__(self):
        """Validação pós-inicialização"""
        if not self.artist_resolvers:
            raise ValueError("artist_resolvers não pode ser None")
        if not self.music_resolvers:
            raise ValueError("music_resolvers não pode ser None") 