install:
	poetry install --with dev
	poetry run pre-commit install -t pre-commit -t commit-msg

lint:
	poetry run pre-commit run --all-files --hook-stage pre-commit
