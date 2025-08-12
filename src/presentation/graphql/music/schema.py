import strawberry
from strawberry.types import Info
from typing import List
from uuid import UUID
from src.presentation.graphql.music.type import MusicType
from src.presentation.graphql.music.input import MusicInput, MusicUpdateInput


# noinspection PyArgumentList
@strawberry.type
class MusicQuery:
    """Query principal do GraphQL"""

    @strawberry.field()
    def musics(self, info: Info) -> List[MusicType]:
        """Obtém todas as músicas"""
        context = info.context
        return context.music_resolvers.get_musics()

    @strawberry.field()
    def music(self, info: Info, music_uuid: UUID) -> MusicType | None:
        """Obtém uma música pelo UUID"""
        context = info.context
        return context.music_resolvers.get_music_by_id(music_uuid)

    @strawberry.field()
    def musics_by_artist(self, info: Info, artist_uuid: UUID) -> List[MusicType]:
        """Obtém todas as músicas de um artista"""
        context = info.context
        return context.music_resolvers.get_musics_by_artist(artist_uuid)


# noinspection PyArgumentList
@strawberry.type
class MusicMutation:
    """Mutation principal do GraphQL"""

    @strawberry.field()
    def delete_artist(self, info: Info, artist_uuid: UUID) -> bool:
        """Deleta um artista"""
        context = info.context
        return context.artist_resolvers.delete_artist(artist_uuid)

    @strawberry.field()
    def create_music(self, info: Info, data: MusicInput) -> MusicType:
        """Cria uma nova música"""
        context = info.context
        return context.music_resolvers.create_music(data)

    @strawberry.field()
    def update_music(
        self, info: Info, music_uuid: UUID, data: MusicUpdateInput
    ) -> MusicType | None:
        """Atualiza uma música"""
        context = info.context
        return context.music_resolvers.update_music(music_uuid, data)

    @strawberry.field()
    def delete_music(self, info: Info, music_uuid: UUID) -> bool:
        """Deleta uma música"""
        context = info.context
        return context.music_resolvers.delete_music(music_uuid)


# noinspection PyArgumentList
@strawberry.type
class MusicSubscription:
    """Subscriptions relacionadas a músicas"""

    @strawberry.subscription()
    async def music_created(self) -> MusicType:
        """Notifica quando uma nova música é criada"""
        pass

    @strawberry.subscription()
    async def music_updated(self, music_uuid: int) -> MusicType:
        """Notifica quando uma música é atualizada"""
        pass

    @strawberry.subscription()
    async def musics_by_artist_updated(self, artist_uuid: int) -> List[MusicType]:
        """Notifica quando músicas de um artista são atualizadas"""
        pass
