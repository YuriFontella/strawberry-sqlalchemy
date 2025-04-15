# API GraphQL com Strawberry e SQLAlchemy

Este documento contém instruções para configurar e executar a API GraphQL que utiliza Strawberry como framework GraphQL e PostgreSQL como banco de dados.

## Pré-requisitos

- Python 3.9+
- PostgreSQL
- pip (gerenciador de pacotes Python)

## Configuração

### 1. Criando o Banco de Dados PostgreSQL

Execute o seguinte comando para criar um banco de dados PostgreSQL:

```bash
createdb nome_do_banco
```

Ou, se preferir usar o psql:

```bash
psql -U postgres
```

Depois, dentro do psql:

```sql
CREATE DATABASE nome_do_banco;
```

### 2. Configurando o arquivo .env

Crie um arquivo `.env` na raiz do projeto com a string de conexão do PostgreSQL:

```
URL=postgresql+psycopg://usuario:senha@localhost:5432/nome_do_banco
```

Substitua `usuario`, `senha` e `nome_do_banco` pelos seus valores específicos.

### 3. Instalando as dependências

Instale todas as dependências necessárias utilizando o pip:

```bash
pip install -r requirements.txt
```

### 4. Iniciando o servidor

Execute o servidor Strawberry com o seguinte comando:

```bash
strawberry server app
```

### 5. Acessando o GraphQL Playground

Após iniciar o servidor, você pode acessar o GraphQL Playground em:

```
http://localhost:8000/graphql
```

## Queries disponíveis

### Adicionar um Artista

```graphql
mutation ($ArtistInput: ArtistInput!) {
  addArtist(data: $ArtistInput) {
    id
    name
  }
}
```

Variáveis:

```json
{
  "ArtistInput": {
    "name": "Nome do Artista"
  }
}
```

### Listar todos os Artistas e suas Músicas

```graphql
query {
  artists {
    name
    musics {
      title
    }
  }
}
```

### Listar todas as Músicas e seus Artistas

```graphql
query {
  musics {
    title
    artist {
      name
    }
  }
}
```

### Adicionar uma Música

```graphql
mutation ($MusicInput: MusicInput!) {
  addMusic(data: $MusicInput) {
    id
    title
  }
}
```

Variáveis:

```json
{
  "MusicInput": {
    "title": "Nome da Música",
    "artistId": 1
  }
}
```