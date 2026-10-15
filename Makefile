.PHONY: test lint format fix ready
PYTHON ?= uv run python

test:
	${PYTHON} -m pytest

lint:
	${PYTHON} -m ruff check .

format:
	${PYTHON} -m ruff format .

fix:
	${PYTHON} -m ruff check . --fix
	${PYTHON} -m ruff format .

ready: fix test lint