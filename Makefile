test:
	pytest

lint:
	isort --check-only app tests
	black --check app tests
	flake8 app tests
	mypy app
