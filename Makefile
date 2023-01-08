run:
	pipenv run python pydo/main.py --config "settings/settings.json" --modules "$(ARGS)"

test:
	pipenv run python -m unittest tests/test_modules.py

clean:
	rm -rf __pycache__

.PHONY: init test
