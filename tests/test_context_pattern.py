"""
Teste da Context Pattern implementada
"""

import pytest
from unittest.mock import Mock
from src.presentation.graphql.context import GraphQLContext
from src.presentation.graphql.resolvers import ArtistResolvers, MusicResolvers


class TestContextPattern:
    """Testes para a Context Pattern"""
    
    def test_context_creation(self):
        """Testa a criação do contexto"""
        artist_resolvers = Mock(spec=ArtistResolvers)
        music_resolvers = Mock(spec=MusicResolvers)
        
        context = GraphQLContext(
            artist_resolvers=artist_resolvers,
            music_resolvers=music_resolvers
        )
        
        assert context.artist_resolvers == artist_resolvers
        assert context.music_resolvers == music_resolvers
    
    def test_context_access(self):
        """Testa o acesso às dependências através do contexto"""
        artist_resolvers = Mock(spec=ArtistResolvers)
        music_resolvers = Mock(spec=MusicResolvers)
        
        context = GraphQLContext(
            artist_resolvers=artist_resolvers,
            music_resolvers=music_resolvers
        )
        
        # Simula o uso em um resolver
        def mock_resolver(info):
            context: GraphQLContext = info.context
            return context.artist_resolvers.get_artists()
        
        # Mock do objeto info
        info = Mock()
        info.context = context
        
        # Executa o resolver
        result = mock_resolver(info)
        
        # Verifica se o método foi chamado
        artist_resolvers.get_artists.assert_called_once()
    
    def test_schema_creation(self):
        """Testa se o schema pode ser criado com sucesso"""
        from src.presentation.graphql.schema import create_schema
        
        schema = create_schema()
        assert schema is not None
        assert hasattr(schema, 'query')
        assert hasattr(schema, 'mutation')
        assert hasattr(schema, 'subscription')
    
    def test_app_creation(self):
        """Testa se a aplicação pode ser criada com sucesso"""
        from main import create_app
        
        app = create_app()
        assert app is not None


if __name__ == "__main__":
    # Executa os testes
    pytest.main([__file__, "-v"]) 