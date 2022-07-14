.PHONY: dev-deps deps format lint help
.DEFAULT_GOAL := help

SERVICE=algorithms

## dev-deps: Install python dev packages
dev-deps:
	pip install -r requirements.dev.txt

## deps: Install python packages
deps:
	pip install -r requirements.txt

## format: Format codebase
format:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place problems data_structures visualization --exclude=__init__.py
	black problems data_structures visualization
	isort problems data_structures visualization --profile black

## lint: Lint codebase
lint:
	black problems data_structures visualization --check
	isort problems data_structures visualization --check-only --profile black
