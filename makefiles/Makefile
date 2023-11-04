.PHONY: docs

help:
	@echo "available commands: install, dev, test, clean, flake, check, docs"
	@echo " - install: install requirements"
	@echo " - dev: install dev requirements"
	@echo " - test: run tests"
	@echo " - clean: remove cache files"
	@echo " - flake: run flake8"
	@echo " - check: run flake8 and tests"
	@echo " - docs: generate documentation"

install:
	pip install -r requirements.txt

dev: install
	pip install -r dev-requirements.txt

test:
	pytest test.py


clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/

flake:
	flake8 main.py test.py

# make flake will run and then make test will run, and then make clean
check: flake test clean

# to generate documentation, --force if folder exists, --html for html format, main specifies the file
docs:
	pdoc --html --force --output-dir docs main