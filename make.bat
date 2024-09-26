@echo off


IF /I "%1"=="test" GOTO test
IF /I "%1"=="build" GOTO build
IF /I "%1"=="install" GOTO install
IF /I "%1"=="upload" GOTO upload
IF /I "%1"=="docs" GOTO docs
IF /I "%1"=="clean" GOTO clean
IF /I "%1"=="format" GOTO format
IF /I "%1"=="setup" GOTO setup
GOTO error

:test
	@coverage run -m unittest discover tests/ -v
	GOTO :EOF

:build
	@rm -rf build build
	@rm -rf build dist
	@rm -rf *.egg-info
	@python -m pip install --upgrade build
	@python -m build --sdist --wheel
	GOTO :EOF

:install
	@python -m pip install --upgrade pip
	@python -m pip install -e .
	GOTO :EOF

:upload
	@python -m twine upload --config-file .pypirc dist/*
	GOTO :EOF

:docs
	@make -C docs html
	GOTO :EOF

:clean
	@rm -rf build dist
	@rm -rf *.egg-info
	@rm -rf .coverage
	@rm -rf .pytest_cache
	@rm -rf .mypy
	GOTO :EOF

:format
	@ruff check --fix
	@ruff format
	GOTO :EOF

:setup
	@python -m pip install --upgrade pip
	@python -m pip install -r requirements.dev.txt
	@pre-commit install
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
