.PHONY: clean run build-docker

NAME = $(shell grep "LABEL name" docker/Dockerfile | cut -d"=" -f2 | sed 's/\"//g')
VERSION = $(shell grep "LABEL version" docker/Dockerfile | cut -d"=" -f2 | sed 's/\"//g')

help:
	@echo "\033[32m.: HELP :."
	@echo "==========\033[0m"
	@echo " - clean		clean *.pyc file"
	@echo " - run			run Flask app"
	@echo " - build-docker		build docker image => $(NAME):$(VERSION)"


clean:
	@find . -type f -name "*.pyc" -delete

run: export FLASK_ENV = dev
run:
	@gunicorn -w 2 -b 0.0.0.0:5000 run:app --log-level debug

build-docker:
	@cp -a Makefile __init__.py api data.csv instance requirements.txt run.py docker/
	@docker build docker/ -t $(NAME):$(VERSION)
