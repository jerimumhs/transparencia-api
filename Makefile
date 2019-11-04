default:
	@echo "Local examples:"
	@echo "  make set-env           # Set the dev enviroment (install deps and create .env)"
	@echo "  make run               # Starts a Flask development server locally"
	@echo "  make shell             # Runs 'flask shell' locally with iPython"
	@echo "  make flake8            # Check code styling with flake8"
	@echo "  make makemigration     # Create a new migration"
	@echo "  make migrate           # Apply a new migration"
	@echo "  make downgrade         # Reverse a migration"

run:
	flask run

shell:
	flask shell

set-env:
	pip install -r requirements-dev.txt
	cp .env.example .env
migrate:
	docker-compose run flask ????

makemigrations:
	docker-compose run flask ????

test:
	docker-compose run flask ????

bash:
	docker-compose run flask bash

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

config.env:
	cp .env.sample .env

db.makemigration:
	flask db migrate

db.migrate:
	flask db upgrade

db.downgrade:
	flask db downgrade

flake8:
	flake8
################################################################################
# Local commands
################################################################################
local.pip.install:
	pip install -r requirements-dev.txt
