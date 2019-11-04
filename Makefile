default:
	@echo "Local examples:"
	@echo "  make set-env           # Set the dev enviroment (install deps and create .env)"
	@echo "  make run               # Starts a Flask development server locally"
	@echo "  make shell             # Runs 'flask shell' locally with iPython"
	@echo "  make flake8            # Check code styling with flake8"
	@echo "  make makemigrations    # Create new migrations"
	@echo "  make migrate           # Apply new migrations"
	@echo "  make downgrade         # Reverse last migrations"

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

################################################################################
# Configuration
################################################################################
pip.install:
	pip install -r requirements-dev.txt

config.env:
	cp .env.sample .env

set-env: config.env pip.install