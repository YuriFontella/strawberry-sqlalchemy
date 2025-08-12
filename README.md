# Strawberry SQLAlchemy - Clean Architecture

API GraphQL usando Strawberry GraphQL e SQLAlchemy seguindo os princípios da **Clean Architecture**.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- SQLite (padrão) ou PostgreSQL

### Instalação

1. Clone e instale as dependências:
```bash
git clone <repository-url>
cd strawberry-sqlalchemy
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
```bash
cp env.example .env
```

3. Execute a aplicação:
```bash
python main.py
```

A aplicação estará disponível em `http://localhost:8000/graphql`

## 🏗️ Arquitetura

```
src/
├── domain/                 # Entidades e interfaces
├── application/           # Casos de uso
├── infrastructure/        # Banco de dados e configurações
└── presentation/         # GraphQL (resolvers, schema)
```

## 📊 Exemplos de Queries

### Queries
```graphql
# Obter todos os artistas
query get_artists {
  artists {
    uuid
    name,
    status
  }
}

# Obter músicas de um artista
query music_by_artist {
  musics_by_artist (artist_uuid: "26077a72-5f1f-4ffe-b1ce-63ab14556cef") {
    uuid
    title
    artist_uuid
  }
}
```

### Mutations
```graphql
# Criar artista
mutation add_artist ($ArtistInput: ArtistInput!) {
  create_artist(data: $ArtistInput) {
    uuid
    name
  }
}
```
```json
{
"ArtistInput": {
    "name": "Eminem"
  }
}
```

```graphql
# Criar música
mutation add_music ($MusicInput: MusicInput!) {
  create_music(data: $MusicInput) {
    uuid
    title
  }
}
```
```json
{
  "MusicInput": {
    "title": "My name is",
    "artist_uuid": "26077a72-5f1f-4ffe-b1ce-63ab14556cef"
  }
}
```

## 🧪 Testes

```bash
pytest tests/
```

## 🔧 Desenvolvimento

### Adicionando Novas Funcionalidades

1. **Entidade**: `src/domain/entities/`
2. **Repositório**: `src/domain/repositories/` (interface) + `src/infrastructure/database/repositories.py` (implementação)
3. **Caso de Uso**: `src/application/use_cases/`
4. **Resolver**: `src/presentation/graphql/resolvers.py`
5. **Container**: Adicione dependências em `src/infrastructure/container.py`

## 📈 Benefícios

- ✅ **Independência de Frameworks**: Domínio não depende de frameworks externos
- ✅ **Testabilidade**: Fácil testar cada camada isoladamente
- ✅ **Independência de UI**: Lógica de negócio independente da interface
- ✅ **Independência de Banco**: Fácil trocar implementações de banco de dados
- ✅ **Separação de Responsabilidades**: Cada camada tem responsabilidade específica