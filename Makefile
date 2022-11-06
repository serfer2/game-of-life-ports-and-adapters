#!/bin/bash
VENV=". venv/bin/activate"
MIN_COVERAGE=100

activate:
	source venv/bin/activate;

test: activate
	pytest --cov-report=term-missing --cov=app tests/ --cov-fail-under=${MIN_COVERAGE}

lint: activate
	isort --check-only app tests
	black --check app tests
	flake8 app tests
	mypy app
