#!/bin/bash -e

docker-compose -f docker-compose.tests.yml down --remove-orphans

docker-compose -f docker-compose.tests.yml build --pull

docker-compose -f docker-compose.tests.yml run -e --rm tests || true

tput setaf 6; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0
echo "Running flake8" | sed  -e :a -e "s/^.\{1,$(tput cols)\}$/ & /;ta" | tr -d '\n' | head -c $(tput cols)
tput setaf 6; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0
docker-compose -f docker-compose.tests.yml run -e --rm flake || true

tput setaf 6; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0
echo "Running mypy" | sed  -e :a -e "s/^.\{1,$(tput cols)\}$/ & /;ta" | tr -d '\n' | head -c $(tput cols)
tput setaf 6; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0
docker-compose -f docker-compose.tests.yml run -e --rm mypy  || true

tput setaf 5; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0
echo "Finished, removing containers" | sed  -e :a -e "s/^.\{1,$(tput cols)\}$/ & /;ta" | tr -d '\n' | head -c $(tput cols)
tput setaf 5; printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =; tput sgr0

docker-compose -f docker-compose.tests.yml down --remove-orphans
