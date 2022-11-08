#!/bin/bash
VENV=". venv/bin/activate"
MIN_COVERAGE=100

activate:
	source venv/bin/activate;

test: activate
	pytest --cov-report=term-missing --cov=src tests/ --cov-fail-under=${MIN_COVERAGE}

lint: activate
	isort --check-only src tests
	black --check src tests
	flake8 src tests
	mypy src
