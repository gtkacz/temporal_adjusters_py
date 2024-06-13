test:
	@coverage run -m unittest discover tests/ -v

build:
	@rm -rf build build
	@rm -rf build dist
	@rm -rf *.egg-info
	@python -m pip install --upgrade build
	@python -m build --sdist --wheel

install:
	@python -m pip install --upgrade pip
	@python -m pip install -e .

deploy:
	@build
	@python -m twine upload dist/*