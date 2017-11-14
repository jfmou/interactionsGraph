.PHONY: clean run build-docker tests

NAME = $(shell grep "LABEL name" docker/Dockerfile | cut -d"=" -f2 | sed 's/\"//g')
VERSION = $(shell grep "LABEL version" docker/Dockerfile | cut -d"=" -f2 | sed 's/\"//g')

help:
	@echo "\033[32m.: HELP :."
	@echo "==========\033[0m"
	@echo " - clean		clean *.pyc file"
	@echo " - run			run Flask app"
	@echo " - tests		run unittests"
	@echo " - build-docker		build docker image => $(NAME):$(VERSION)"


clean:
	@ls docker/ | grep -v "Dockerfile\|entrypoint.sh" | sed "s/^/docker\//g" | xargs rm -rf
	@find . -type f -name "*.pyc" -delete

run: export FLASK_ENV = dev
run:
	@##python run.py
	@gunicorn -w 2 -b 0.0.0.0:5000 run:app --log-level debug

build-docker: clean
	@cp -a Makefile __init__.py api instance requirements.txt run.py docker/
	@rm -rf docker/api/static/uploads/*
	@rm -rf docker/api/static/csv/*
	@docker build docker/ -t $(NAME):$(VERSION)

tests: export FLASK_ENV = test
tests:
	@sh tests.sh
