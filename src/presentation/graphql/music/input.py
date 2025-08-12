import strawberry

from src.domain.entities.music import Music


@strawberry.input
class MusicInput(Music):
    """Input GraphQL para Music"""


@strawberry.input
class MusicUpdateInput(Music):
    """Input GraphQL para atualização de Music"""
