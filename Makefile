test:
	python -m pytest tests/test_colors.py -q

lint:
	python -m pylint tensorhue

.PHONY: test lint
