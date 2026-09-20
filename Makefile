.PHONY: install lint format test build deploy

install:
	#install dependencies
	uv sync
lint:
	#check linting error
	uv run pylint --disable=R,C *.py mylib/*.py
format:
	#format code structure
	uv run black *.py mylib/*.py
test:
	#test code
	uv run pytest -vv
build:
	#build code
deploy:
	#code deploy
