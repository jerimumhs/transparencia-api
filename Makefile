################################################################################
# Docker-compose api-server service commands for dev
################################################################################

run:
	docker-compose run api-server $(cmd)

flake8:
	docker-compose run api-server flake8

migrate:
	docker-compose run api-server ????

makemigrations:
	docker-compose run api-server ????

test:
	echo 'TEST!'

bash:
	docker-compose run api-server bash

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

config.env:
	cp .env.example .env

current_dir = $(notdir $(shell pwd))
remove.volumes:
	docker-compose down
	docker volume rm $(current_dir)_pg_volume

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop

################################################################################
# Local commands
################################################################################
local.pip.install:
	pip install -r requirements/local.txt

################################################################################
# Heroku commands
################################################################################
deploy:
	git push heroku
