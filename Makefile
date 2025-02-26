.PHONY: setup

test:
	@coverage run -m unittest discover tests/ -v
	@coverage report -m

build:
	@rm -rf build build
	@rm -rf build dist
	@rm -rf *.egg-info
	@python -m pip install --upgrade build
	@python -m build --sdist --wheel

install:
	@python -m pip install --upgrade pip
	@python -m pip install -e .

upload:
	@python -m twine upload --config-file .pypirc dist/*

docs:
	@make -C docs html

clean:
	@rm -rf build dist
	@rm -rf *.egg-info
	@rm -rf .coverage
	@rm -rf .pytest_cache
	@rm -rf .mypy

format:
	@ruff check --fix
	@ruff format

setup:
	@python -m pip install --upgrade pip
	@python -m pip install -r requirements.dev.txt
	@pre-commit install
