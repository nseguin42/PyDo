run:
	export PYTHONPATH="$PWD/pydo"
	pipenv run python pydo/main.py --config "settings/settings.json"

test:
	export PYTHONPATH="$PWD/pydo; $PWD/tests"
	pipenv run python -m unittest tests/test_modules.py

clean:
	rm -rf __pycache__

.PHONY: init test
