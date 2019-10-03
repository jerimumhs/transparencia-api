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

db.makemigration:
	flask db migrate

db.migrate:
	flask db upgrade

db.downgrade:
	flask db downgrade

flake8:
	flake8
