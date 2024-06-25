.PHONY: clean-pyc

build: clean-pyc
	docker-compose build deloreans-build

run: build clean-container
	docker-compose up -d deloreans-run

ssh:
	docker-compose exec deloreans-run /bin/sh

test:
	poetry run python -m pytest -sv --cov-report term-missing --cov-report html:coverage_report --cov-report xml:coverage_report/cov.xml --junitxml=coverage_report/pytest.xml --cov=deloreans/ --disable-warnings -p no:cacheprovider tests/*

testd: build clean-container
	docker-compose up --exit-code-from deloreans-test deloreans-test

lint:
	poetry run python -m flake8 deloreans/ tests/

lintd: build clean-container
	docker-compose up --exit-code-from deloreans-lint deloreans-lint

type-hint:
	poetry run python -m mypy deloreans/

type-hintd: build clean-container
	docker-compose up --exit-code-from deloreans-type-hint deloreans-type-hint

clean-pyc:
	# clean all pyc files
	find . -name '__pycache__' | xargs rm -rf | cat
	find . -name '*.pyc' | xargs rm -f | cat

clean-container:
	# stop and remove useless containers
	docker-compose down --remove-orphans
