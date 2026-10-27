.PHONY: validate test sync-bdd

sync-bdd:
	python3 scripts/sync_bdd_references.py

validate:
	gh skill publish --dry-run
	claude plugin validate .claude-plugin/marketplace.json
	claude plugin validate .

test:
	python3 -m unittest discover -s tests -v
