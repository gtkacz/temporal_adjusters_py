.PHONY: setup test build install upload docs clean format

test:
	@uv run coverage run -m unittest discover tests/ -v
	@uv run coverage report -m

build:
	@rm -rf dist
	@uv build

install:
	@uv sync

upload:
	@uv publish

docs:
	@uv run --group docs make -C docs html

clean:
	@rm -rf build dist
	@rm -rf *.egg-info
	@rm -rf .coverage
	@rm -rf .pytest_cache
	@rm -rf .mypy

format:
	@uv run ruff check --fix
	@uv run ruff format

setup:
	@uv sync --all-groups
	@uv run pre-commit install
