.PHONY: validate test sync-bdd

sync-bdd:
	python3 scripts/sync_bdd_references.py

validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v
