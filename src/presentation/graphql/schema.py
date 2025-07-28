import strawberry
from strawberry.types import Info
from typing import List
from .types import ArtistType, MusicType
from .inputs import ArtistInput, MusicInput, ArtistUpdateInput, MusicUpdateInput


@strawberry.type
class Query:
    """Query principal do GraphQL"""

    @strawberry.field
    def hello(self) -> str:
        """Query de teste"""
        return 'Hello from Clean Architecture!'

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
class Mutation:
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
class Subscription:
    """Subscription principal do GraphQL"""

    @strawberry.subscription
    def count(self, target: int = 100) -> int:
        """Contador simples para demonstração"""
        for i in range(target):
            yield i


def create_schema() -> strawberry.Schema:
    """Cria o schema GraphQL"""
    query = Query()
    mutation = Mutation()
    subscription = Subscription()

    return strawberry.Schema(
        query=query,
        mutation=mutation,
        subscription=subscription
    )