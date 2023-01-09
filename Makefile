run:
	export PYTHONPATH="$PWD/pydo"
	pipenv run python pydo/main.py --config "settings/settings.json" --tasks $(ARGS)

test:
	export PYTHONPATH="$PWD/pydo; $PWD/tests"
	pipenv run python -m unittest tests/test_tasks.py

clean:
	rm -rf __pycache__

.PHONY: init test
