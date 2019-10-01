################################################################################
# Docker-compose flask service commands for dev
################################################################################

run:
	docker-compose run flask $(cmd)

flake8:
	docker-compose run flask flake8

db.init:
	docker-compose run flask flask db init

db.migrate:
	docker-compose run flask flask db migrate

db.upgrade:
	docker-compose run flask flask db upgrade

test:
	docker-compose run flask python -m unittest discover

bash:
	docker-compose run flask bash

shell:
	docker-compose run flask flask shell

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
	docker volume rm $(current_dir)_postgres_data

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
