current_dir = $(notdir $(shell pwd))

default:
	@echo "Local examples:"
	@echo "  make env.set           # Set the dev environment (install deps and create .env)"
	@echo "  make run               # Starts a Flask development server locally"
	@echo "  make shell             # Runs 'flask shell' locally with iPython"
	@echo "  make flake8            # Check code styling with flake8"
	@echo "  make test              # Runs test suite"
	@echo "  make makemigrations    # Create new migrations"
	@echo "  make migrate           # Apply new migrations"
	@echo "  make downgrade         # Reverse last migrations"

	@echo "Docker examples:"
	@echo "  make env.cp                            # Set the dev environment (create .env)"
	@echo "  make docker.build                      # Build docker image"
	@echo "  make docker.up                         # Start docker-compose services"
	@echo "  make docker.down                       # Stop docker-compose services"
	@echo "  make docker.logs                       # Connect to docker-compose services logs"
	@echo "  make docker.bash                       # Runs 'bash' on api-server service"
	@echo "  make docker.shell                      # Runs 'flask shell' on api-server service"
	@echo "  make docker.flake8                     # Check code styling with flake8 on api-server service"
	@echo "  make docker.test                       # Runs test suite on api-server service"
	@echo "  make docker.makemigrations             # Create new migrations"
	@echo "  make docker.migrate                    # Apply new migrations"
	@echo "  make docker.docker.api-server.stop     # Stop docker-compose api-server service"
	@echo "  make docker.docker.api-server.restart  # Restart docker-compose api-server service"
	@echo "  make docker.volumes.remove             # Stop services and remove db volume"
	@echo "  make docker.clear                      # Stop all docker containers on machine"

################################################################################
# Configuration
################################################################################
pip.install:
	pip install -r requirements-dev.txt

env.cp:
	cp .env.sample .env

env.set: env.cp pip.install

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

test:
	echo 'TEST'

################################################################################
# Docker-compose api-server service commands for dev
################################################################################
docker.build:
	docker-compose build

docker.logs:
	docker-compose logs -f

docker.up:
	docker-compose up -d

docker.down:
	docker-compose down

docker.bash:
	docker-compose run api-server bash

docker.shell:
	docker-compose run api-server flask shell

docker.test:
	docker-compose run api-server echo 'TEST'

docker.flake8:
	docker-compose run api-server flake8

docker.makemigrations:
	docker-compose run api-server flask db migrate

docker.migrate:
	docker-compose run api-server flask db upgrade

docker.downgrade:
	docker-compose run api-server flask db downgrade

docker.api-server.stop:
	docker stop api-server

docker.api-server.restart: docker.bot.stop docker.up

docker.volumes.remove: docker.down
	docker volume rm $(current_dir)_pg_volume

docker.clear:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
