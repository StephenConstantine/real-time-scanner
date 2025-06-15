.PHONY: test test-unit test-integration test-all test-coverage test-fast clean install dev-install lint format type-check

# Test commands
test: test-unit

test-unit:
	@echo "Running unit tests..."
	python3 run_tests.py --type unit

test-integration:
	@echo "Running integration tests..."
	python3 run_tests.py --type integration

test-all:
	@echo "Running all tests..."
	python3 run_tests.py --type all

test-fast:
	@echo "Running fast tests..."
	python3 run_tests.py --type fast

test-coverage:
	@echo "Running tests with coverage..."
	python3 run_tests.py --type coverage

test-html-coverage:
	@echo "Running tests with HTML coverage report..."
	python3 run_tests.py --html-coverage

test-verbose:
	@echo "Running tests with verbose output..."
	python3 run_tests.py --verbose

# Quick test commands
test-models:
	@echo "Testing models..."
	python3 -m pytest tests/test_models.py -v

test-utils:
	@echo "Testing utils..."
	python3 -m pytest tests/test_utils.py -v

# Development commands
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

dev-install: install
	@echo "Installing development dependencies..."
	pip install black flake8 mypy pytest-cov coverage

lint:
	@echo "Running linter..."
	flake8 modules/ tests/ --max-line-length=88 --ignore=E203,W503

format:
	@echo "Formatting code..."
	black modules/ tests/ run_tests.py

type-check:
	@echo "Running type checker..."
	mypy modules/ --ignore-missing-imports

# Cleanup
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__/
	rm -rf modules/__pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

# Help
help:
	@echo "Available commands:"
	@echo "  test           - Run unit tests (default)"
	@echo "  test-unit      - Run unit tests"
	@echo "  test-integration - Run integration tests"
	@echo "  test-all       - Run all tests"
	@echo "  test-fast      - Run fast tests only"
	@echo "  test-coverage  - Run tests with coverage"
	@echo "  test-html-coverage - Generate HTML coverage report"
	@echo "  test-verbose   - Run tests with verbose output"
	@echo "  test-models    - Test models only"
	@echo "  test-utils     - Test utils only"
	@echo "  install        - Install dependencies"
	@echo "  dev-install    - Install dev dependencies"
	@echo "  lint           - Run linter"
	@echo "  format         - Format code"
	@echo "  type-check     - Run type checker"
	@echo "  clean          - Clean up generated files"
	@echo "  help           - Show this help"

