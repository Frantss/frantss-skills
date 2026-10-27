.PHONY: validate test sync-bdd

sync-bdd:
	python3 scripts/sync_bdd_references.py

validate:
	gh skill publish --dry-run
	claude plugin validate .
	@for plugin in plugins/*; do \
		claude plugin validate "$$plugin" || exit $$?; \
	done

test:
	python3 -m unittest discover -s tests -v
