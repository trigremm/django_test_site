MAIN_BACKEND_SERVICE=django_main
MAIN_BACKEND_PATH=django_app

# default
all: ps

# general
ps:
	docker compose ps

logs:
	@while True; do \
		docker compose logs -f --tail 100; \
		sleep 10; \
	done

prune:
	docker system prune -f -a

config:
	docker compose config

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

stop-backend:
	docker compose stop ${MAIN_BACKEND_SERVICE}

down:
	docker compose down --remove-orphans

restart: stop-backend up

recreate: pull build stop up ps

r: recreate

# shell
shell:
	docker compose exec ${MAIN_BACKEND_SERVICE} bash

runshell:
	docker compose run ${MAIN_BACKEND_SERVICE} bash

ishell:
	docker compose exec ${MAIN_BACKEND_SERVICE} sh -c 'pip install ipython && python manage.py shell'

# format
format: add_file_path_comment
	# pip install isort black pylint bandit mypy flake8 pytest coverage safety pre-commit types-requests pydocstyle radon
	# pre-commit install

	# imports sorting
	@python -m isort ${MAIN_BACKEND_PATH}/ --line-width 120 --quiet
	
	# code formatting
	@python -m black ${MAIN_BACKEND_PATH}/ --line-length 120 --quiet

f: format

add_file_path_comment:
	@python utils.d/add_file_path_comment.py
	@echo "file path comment added"

prompt:
	@bash utils.d/generate_prompt.sh -i migrations -p ./${MAIN_BACKEND_PATH}
	@echo "prompt generated"

.PHONY: all config ps logs logs_forever prune
.PHONY: pull pull-images
.PHONY: build rebuild cached-build
.PHONY: up run stop down restart r
.PHONY: recreate recreate-backend rb
.PHONY: shell runshell ishell irunshell
.PHONY: format f
.PHONY: add_file_path_comment prompt
