#!/bin/bash -e

docker-compose down --remove-orphans

docker-compose build --pull

docker-compose run -e --rm tests
docker-compose run -e --rm flake
docker-compose run -e --rm mypy

docker-compose down --remove-orphans
