.PHONY: validate test

validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v
