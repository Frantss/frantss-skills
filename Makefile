.PHONY: validate test eval-setup eval-ship-it

validate:
	gh skill publish --dry-run
	claude plugin validate .claude-plugin/marketplace.json
	claude plugin validate .

test:
	python3 -m unittest discover -s tests -v

eval-setup:
	python3 -m venv .scratch/evals/venv
	.scratch/evals/venv/bin/python -m pip install -r evals/requirements.txt

eval-ship-it:
	.scratch/evals/venv/bin/python evals/ship_it.py $(EVAL_ARGS)
