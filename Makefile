.PHONY: setup test lint check

setup:
	uv sync --frozen

test:
	uv run pytest -q

lint:
	uv run ruff check .
	uv run ruff format --check .

check: lint test
