import strawberry
from strawberry.types import Info
from typing import List
from .type import MusicType
from .input import MusicInput, MusicUpdateInput


@strawberry.type
class MusicQuery:
    """Query principal do GraphQL"""

    @strawberry.field
    def musics(self, info: Info) -> List[MusicType]:
        """Obtém todas as músicas"""
        context = info.context
        return context.music_resolvers.get_musics()

    @strawberry.field
    def music(self, info: Info, music_id: int) -> MusicType | None:
        """Obtém uma música pelo ID"""
        context = info.context
        return context.music_resolvers.get_music_by_id(music_id)

    @strawberry.field
    def musics_by_artist(self, info: Info, artist_id: int) -> List[MusicType]:
        """Obtém todas as músicas de um artista"""
        context = info.context
        return context.music_resolvers.get_musics_by_artist(artist_id)


@strawberry.type
class MusicMutation:
    """Mutation principal do GraphQL"""

    @strawberry.field
    def delete_artist(self, info: Info, artist_id: int) -> bool:
        """Deleta um artista"""
        context = info.context
        return context.artist_resolvers.delete_artist(artist_id)

    @strawberry.field
    def create_music(self, info: Info, data: MusicInput) -> MusicType:
        """Cria uma nova música"""
        context = info.context
        return context.music_resolvers.create_music(data)

    @strawberry.field
    def update_music(self, info: Info, music_id: int, data: MusicUpdateInput) -> MusicType | None:
        """Atualiza uma música"""
        context = info.context
        return context.music_resolvers.update_music(music_id, data)

    @strawberry.field
    def delete_music(self, info: Info, music_id: int) -> bool:
        """Deleta uma música"""
        context = info.context
        return context.music_resolvers.delete_music(music_id)


@strawberry.type
class MusicSubscription:
    """Subscriptions relacionadas a músicas"""

    @strawberry.subscription
    async def music_created(self) -> MusicType:
        """Notifica quando uma nova música é criada"""
        pass

    @strawberry.subscription
    async def music_updated(self, music_id: int) -> MusicType:
        """Notifica quando uma música é atualizada"""
        pass

    @strawberry.subscription
    async def musics_by_artist_updated(self, artist_id: int) -> List[MusicType]:
        """Notifica quando músicas de um artista são atualizadas"""
        pass

