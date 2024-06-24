.PHONY: clean-pyc

build: clean-pyc
	docker-compose build delorean-build

run: build clean-container
	docker-compose up -d delorean-run

ssh:
	docker-compose exec delorean-run /bin/sh

test:
	poetry run python -m pytest -sv --cov-report term-missing --cov-report html:coverage_report --cov-report xml:coverage_report/cov.xml --junitxml=coverage_report/pytest.xml --cov=delorean/ --disable-warnings -p no:cacheprovider tests/*

testd: build clean-container
	docker-compose up --exit-code-from delorean-test delorean-test

lint:
	poetry run python -m flake8 delorean/ tests/

lintd: build clean-container
	docker-compose up --exit-code-from delorean-lint delorean-lint

type-hint:
	poetry run python -m mypy delorean/

type-hintd: build clean-container
	docker-compose up --exit-code-from delorean-type-hint delorean-type-hint

clean-pyc:
	# clean all pyc files
	find . -name '__pycache__' | xargs rm -rf | cat
	find . -name '*.pyc' | xargs rm -f | cat

clean-container:
	# stop and remove useless containers
	docker-compose down --remove-orphans
