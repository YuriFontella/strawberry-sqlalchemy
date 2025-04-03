```
docker build -t upbet/originals:platform-graphql -f Dockerfile .
```
```
docker-compose -p platform-graphql -f docker-compose.yaml up -d
```
ARM64
```
docker buildx build --platform linux/amd64,linux/arm64 -t upbet/originals:platform-graphql --push .
```