import strawberry
from strawberry.types import Info
from typing import List
from .type import ArtistType
from .input import ArtistInput, ArtistUpdateInput


@strawberry.type
class ArtistQuery:
    """Query principal do GraphQL"""

    @strawberry.field
    def artists(self, info: Info) -> List[ArtistType]:
        """Obtém todos os artistas"""
        context = info.context
        return context.artist_resolvers.get_artists()

    @strawberry.field
    def artist(self, info: Info, artist_id: int) -> ArtistType | None:
        """Obtém um artista pelo ID"""
        context = info.context
        return context.artist_resolvers.get_artist_by_id(artist_id)

    @strawberry.field
    def active_artists(self, info: Info) -> List[ArtistType]:
        """Obtém apenas artistas ativos"""
        context = info.context
        return context.artist_resolvers.get_active_artists()


@strawberry.type
class ArtistMutation:
    """Mutation principal do GraphQL"""

    @strawberry.field
    def create_artist(self, info: Info, data: ArtistInput) -> ArtistType:
        """Cria um novo artista"""
        context = info.context
        return context.artist_resolvers.create_artist(data)

    @strawberry.field
    def update_artist(self, info: Info, artist_id: int, data: ArtistUpdateInput) -> ArtistType | None:
        """Atualiza um artista"""
        context = info.context
        return context.artist_resolvers.update_artist(artist_id, data)

    @strawberry.field
    def delete_artist(self, info: Info, artist_id: int) -> bool:
        """Deleta um artista"""
        context = info.context
        return context.artist_resolvers.delete_artist(artist_id)

    @strawberry.field
    def delete_music(self, info: Info, music_id: int) -> bool:
        """Deleta uma música"""
        context = info.context
        return context.music_resolvers.delete_music(music_id)


@strawberry.type
class ArtistSubscription:
    """Subscriptions relacionadas a artistas"""

    @strawberry.subscription
    async def artist_created(self) -> ArtistType:
        """Notifica quando um novo artista é criado"""
        # Implementação de subscription em tempo real
        # Aqui você integraria com um sistema de eventos/pub-sub
        pass

    @strawberry.subscription
    async def artist_updated(self, artist_id: int) -> ArtistType:
        """Notifica quando um artista é atualizado"""
        pass
