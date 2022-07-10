.PHONY: dev-deps deps format lint build-docker run-docker run-cli run-api test test-with-coverage help
.DEFAULT_GOAL := help

SERVICE=kayak-challenge
IMAGE=$(SERVICE):latest

## dev-deps: Install python dev packages
dev-deps:
	pip install -r requirements.dev.txt

## deps: Install python packages
deps:
	pip install -r requirements.txt

## format: Format codebase
format:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place problems data_structures graphviz --exclude=__init__.py
	black problems data_structures graphviz
	isort problems data_structures graphviz --profile black

## lint: Lint codebase
lint:
	black problems data_structures graphviz --check
	isort problems data_structures graphviz --check-only --profile black
