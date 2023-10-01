all: ps

# general
config:
	docker compose config

ps:
	docker compose ps

logs:
	docker compose logs -f --tail 100

logs_forever:
	while True; do \
		docker compose logs -f --tail 100; \
		sleep 10; \
	done

prune:
	docker system prune -f -a

# build
pull:
	git pull

pull-images:
	docker compose pull

build:
	# docker compose build --no-cache --pull
	docker compose build 

# run
up:
	docker compose up -d --no-build

stop:
	docker compose stop

down:
	docker compose down --remove-orphans

restart: stop up

recreate: pull build stop up ps

# shell
shell:
	docker compose exec django_main bash

runshell:
	docker compose run django_main bash

ishell:
	docker compose exec django_main sh -c 'pip install ipython && python manage.py shell'

# format
format: add_file_path_comment
	# pip install isort black pylint bandit mypy flake8 pytest coverage safety pre-commit types-requests pydocstyle radon
	# pre-commit install

	# imports sorting
	@python -m isort django_app/ --line-width 120 --quiet
	
	# code formatting
	@python -m black django_app/ --line-length 120 --quiet

add_file_path_comment:
	@python utils.d/add_file_path_comment.py
	@echo "file path comment added"

prompt:
	@bash utils.d/generate_prompt.sh -i migrations -p ./django_app
	@echo "prompt generated"

.PHONY: all config ps logs logs_forever prune
.PHONY: pull pull-images
.PHONY: build rebuild cached-build
.PHONY: up run stop down restart
.PHONY: recreate recreate-backend rb
.PHONY: shell runshell ishell irunshell
.PHONY: format
.PHONY: add_file_path_comment prompt
