all:

# Serve app with uvicorn
.PHONY: serve
serve:
	python resume_builder/app.py

# Reformat code
.PHONY: black
black:
	black .

# Tests (unit with pytest)
.PHONY: pytest
pytest:
	pytest tests/

# Test code linting
.PHONY: black_test
black_test:
	black --check .
