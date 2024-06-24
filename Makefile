.PHONY: clean-pyc

build: clean-pyc
	docker-compose build delorean-build

run: build clean-container
	docker-compose up -d delorean-run

ssh:
	docker-compose exec delorean-run /bin/sh

test:
	python -m pytest -sv --cov-report term-missing --disable-warnings -p no:cacheprovider tests/*

testd: build clean-container
	docker-compose up --exit-code-from delorean-test delorean-test

clean-pyc:
	# clean all pyc files
	find . -name '__pycache__' | xargs rm -rf | cat
	find . -name '*.pyc' | xargs rm -f | cat

clean-container:
	# stop and remove useless containers
	docker-compose down --remove-orphans
