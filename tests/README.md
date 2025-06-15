# Test System Documentation

This directory contains the comprehensive test suite for the Real-Time Event Exploration System.

## Overview

The test system is designed to be:
- **Fast**: Unit tests run quickly for rapid development feedback
- **Comprehensive**: Full coverage of data models, utilities, and business logic
- **Reliable**: Isolated tests with proper mocking and fixtures
- **Maintainable**: Clear structure and well-documented test cases

## Test Structure

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Pytest configuration and shared fixtures
├── test_models.py           # Data model tests
├── test_utils.py            # Utility function tests
└── README.md               # This file
```

## Running Tests

### Using Makefile (Recommended)

```bash
# Run all unit tests (default)
make test

# Run specific test types
make test-unit           # Unit tests only
make test-integration    # Integration tests only
make test-all           # All tests
make test-fast          # Fast tests only (excludes slow/network/ai tests)

# Coverage reports
make test-coverage       # Run with coverage report
make test-html-coverage  # Generate HTML coverage report

# Test specific modules
make test-models        # Test models only
make test-utils         # Test utils only

# Development
make test-verbose       # Verbose output
```

### Using Test Runner Script

```bash
# Basic usage
python3 run_tests.py --type unit

# With options
python3 run_tests.py --type all --verbose --coverage
python3 run_tests.py --file test_models.py
python3 run_tests.py --function "test_creation"
```

### Direct Pytest

```bash
# Run all tests
python3 -m pytest

# Run specific test file
python3 -m pytest tests/test_models.py

# Run specific test
python3 -m pytest tests/test_models.py::TestTrendingEvent::test_creation

# With coverage
python3 -m pytest --cov=modules --cov-report=html
```

## Test Categories

Tests are organized with pytest markers:

- `@pytest.mark.unit` - Fast unit tests (default)
- `@pytest.mark.integration` - Integration tests requiring multiple components
- `@pytest.mark.slow` - Slow-running tests
- `@pytest.mark.network` - Tests requiring network access
- `@pytest.mark.ai` - Tests requiring AI/OpenAI API access

## Test Fixtures

The `conftest.py` file provides comprehensive fixtures:

### Core Fixtures
- `temp_dir` - Temporary directory for file operations
- `mock_config` - Mock system configuration
- `mock_prompts_file` - Mock prompts file for testing
- `mock_results_dir` - Mock results directory

### Data Model Fixtures
- `sample_trending_event` - Sample TrendingEvent instance
- `sample_search_queries` - Sample SearchQuery instances
- `sample_event_analysis` - Sample EventAnalysis instance
- `sample_content_items` - Sample content items (Twitter, YouTube, etc.)
- `sample_normalized_data` - Sample NormalizedData instance
- `sample_geo_coordinate` - Sample GeoCoordinate instance
- `sample_map_ready_items` - Sample MapReadyItem instances
- `sample_youmap_payload` - Sample YouMapPayload instance
- `sample_api_response` - Sample APIResponse instance

## Test Files

### test_models.py
Tests all data models for:
- Proper instantiation
- Field validation
- Type safety
- Required vs optional fields
- Inheritance relationships

### test_utils.py
Tests utility functions for:
- File operations (save/load results)
- Prompt loading
- User interaction
- String sanitization
- Timestamp formatting

## Writing New Tests

### Test Class Structure
```python
class TestYourModule:
    """Test YourModule functionality."""
    
    def test_basic_functionality(self):
        """Test basic functionality."""
        # Arrange
        input_data = "test"
        
        # Act
        result = your_function(input_data)
        
        # Assert
        assert result == expected_output
    
    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError, match="Expected error message"):
            your_function(invalid_input)
```

### Using Fixtures
```python
def test_with_fixture(self, sample_trending_event, temp_dir):
    """Test using fixtures."""
    # Use the fixtures in your test
    assert sample_trending_event.title == "Test Event"
    assert os.path.exists(temp_dir)
```

### Mocking External Dependencies
```python
@patch('modules.utils.requests.get')
def test_api_call(self, mock_get):
    """Test API call with mocking."""
    mock_get.return_value.json.return_value = {"data": "test"}
    result = your_api_function()
    assert result["data"] == "test"
```

## Coverage Reports

Coverage reports show which lines of code are tested:

- **Terminal Report**: Shows coverage percentages and missing lines
- **HTML Report**: Detailed interactive report in `htmlcov/index.html`

Target coverage: **90%+** for core modules

## Best Practices

### Test Naming
- Use descriptive test names: `test_should_save_result_when_valid_data_provided`
- Group related tests in classes
- Use consistent naming patterns

### Test Structure
- Follow Arrange-Act-Assert pattern
- One assertion per test when possible
- Test both positive and negative cases

### Mocking
- Mock external dependencies (APIs, file system, databases)
- Use fixtures for reusable test data
- Keep mocks simple and focused

### Performance
- Keep unit tests fast (< 100ms each)
- Use markers for slow tests
- Avoid unnecessary setup/teardown

### Maintenance
- Update tests when changing functionality
- Remove obsolete tests
- Keep test data realistic but minimal

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure PYTHONPATH includes project root
2. **Fixture Not Found**: Check `conftest.py` for fixture definitions
3. **Slow Tests**: Use appropriate markers and run specific test types
4. **Coverage Issues**: Check for missing `__init__.py` files

### Debug Commands
```bash
# Run with maximum verbosity
python3 -m pytest -vvv --tb=long

# Run specific test with output
python3 -m pytest tests/test_utils.py::TestLoadPrompt::test_load_existing_prompt -s

# Show available fixtures
python3 -m pytest --fixtures
```

## Integration with CI/CD

The test system is designed to work with continuous integration:

```yaml
# Example GitHub Actions workflow
- name: Run Tests
  run: |
    python3 run_tests.py --type fast --coverage
    
- name: Upload Coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

## Future Enhancements

- [ ] Add integration tests for complete workflows
- [ ] Add performance/benchmark tests
- [ ] Add property-based testing with Hypothesis
- [ ] Add mutation testing for test quality assessment
- [ ] Add visual regression tests for any UI components

