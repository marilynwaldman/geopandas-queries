# Docker for anaconda::geopandas

https://github.com/jjpanda/docker-geopandas

### Prerequisites
- Host machine running Docker
- Docker has been configured for windows shared drive
- Install compose if using docker-compose

## Execution Instructions - Docker
```
## Docker build
docker build -t geopandas_query .

## Docker run

# For linux
docker run --rm --name query -p 8000:8000  geopandas_query
```
For any changes in test.py, you need to re-execute docker build and then docker run.

## Execution Instructions - docker-compose
```
docker-compose up
docker container ls
```
