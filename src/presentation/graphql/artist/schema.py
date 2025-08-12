import asyncio
import strawberry
from uuid import UUID
from strawberry.types import Info
from typing import List, AsyncGenerator
from src.presentation.graphql.artist.type import ArtistType
from src.presentation.graphql.artist.input import ArtistInput, ArtistUpdateInput

# Lista de consumidores conectados
connected_consumers = []


@strawberry.type
class ArtistQuery:
    """Query principal do GraphQL"""

    @strawberry.field()
    def artists(self, info: Info) -> List[ArtistType]:
        """Obtém todos os artistas"""
        context = info.context
        return context.artist_resolvers.get_artists()

    @strawberry.field()
    def artist(self, info: Info, artist_uuid: UUID) -> ArtistType | None:
        """Obtém um artista pelo UUID"""
        context = info.context
        return context.artist_resolvers.get_artist_by_id(artist_uuid)

    @strawberry.field()
    def active_artists(self, info: Info) -> List[ArtistType]:
        """Obtém apenas artistas ativos"""
        context = info.context
        return context.artist_resolvers.get_active_artists()


@strawberry.type
class ArtistMutation:
    """Mutation principal do GraphQL"""

    @strawberry.field()
    def create_artist(self, info: Info, data: ArtistInput) -> ArtistType:
        """Cria um novo artista"""
        context = info.context
        artist = context.artist_resolvers.create_artist(data)

        # Notifica todos os consumidores conectados
        for queue in connected_consumers:
            queue.put_nowait(artist)

        return artist

    @strawberry.field()
    def update_artist(
        self, info: Info, artist_uuid: UUID, data: ArtistUpdateInput
    ) -> ArtistType | None:
        """Atualiza um artista"""
        context = info.context
        return context.artist_resolvers.update_artist(artist_uuid, data)

    @strawberry.field()
    def delete_artist(self, info: Info, artist_uuid: UUID) -> bool:
        """Deleta um artista"""
        context = info.context
        return context.artist_resolvers.delete_artist(artist_uuid)

    @strawberry.field()
    def delete_music(self, info: Info, music_uuid: UUID) -> bool:
        """Deleta uma música"""
        context = info.context
        return context.music_resolvers.delete_music(music_uuid)


@strawberry.type
class ArtistSubscription:
    """Subscriptions relacionadas a artistas"""

    @strawberry.subscription()
    async def artist_created(self) -> AsyncGenerator[ArtistType, None]:
        """Notifica quando um novo artista é criado"""

        queue = asyncio.Queue()
        connected_consumers.append(queue)

        try:
            while True:
                artist = await queue.get()
                yield artist
        finally:
            connected_consumers.remove(queue)
