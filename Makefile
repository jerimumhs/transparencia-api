default:
	@echo "Local examples:"
	@echo "  make set-env           # Set the dev enviroment (install deps and create .env)"
	@echo "  make run               # Starts a Flask development server locally"
	@echo "  make shell             # Runs 'flask shell' locally with iPython"
	@echo "  make flake8            # Check code styling with flake8"
	@echo "  make makemigrations    # Create new migrations"
	@echo "  make migrate           # Apply new migrations"
	@echo "  make downgrade         # Reverse last migrations"
################################################################################
# Docker-compose api-server service commands for dev
################################################################################

run:
	flask run

shell:
	flask shell

makemigrations:
	flask db migrate

migrate:
	flask db upgrade

downgrade:
	flask db downgrade

flake8:
	flake8

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf
clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
current_dir = $(notdir $(shell pwd))
remove.volumes:
	docker-compose down
	docker volume rm $(current_dir)_pg_volume
################################################################################
# Configuration
################################################################################
pip.install:
	pip install -r requirements-dev.txt

config.env:
	cp .env.sample .env

set-env: config.env pip.install