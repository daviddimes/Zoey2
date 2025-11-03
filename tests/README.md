# Testing Guide for Zoey2


This document provides information about the unit tests for the Zoey2 Telegram bot project.

## Overview

The test suite provides comprehensive coverage for the bot's functionality, including:

- **Environment variable handling** - Testing bot token loading and validation
- **Command handlers** - Testing the `/start` command and response handling
- **Application setup** - Testing the main function and Telegram application initialization
- **Error handling** - Testing edge cases and error scenarios
- **Integration tests** - Testing the complete bot workflow

## Test Structure

Tests are organized into the following classes:

### TestBotInitialization
- `test_bot_token_from_env` - Verifies bot token is loaded from environment
- `test_bot_token_missing_raises_error` - Ensures proper error handling for missing token
- `test_load_dotenv_called` - Confirms dotenv is called during module import

### TestStartCommandHandler
- `test_start_command_success` - Tests successful `/start` command handling
- `test_start_command_no_message` - Tests behavior when update has no message
- `test_start_command_reply_error_handling` - Tests error handling in message replies

### TestMainFunction
- `test_main_function_creates_application` - Verifies Telegram application creation
- `test_main_function_adds_command_handler` - Confirms command handler registration
- `test_main_function_starts_polling` - Tests polling initialization

### TestIntegration
- `test_end_to_end_bot_setup` - Complete bot setup workflow test
- `test_start_command_integration` - Integration test for start command

### TestErrorHandling
- `test_start_with_invalid_update` - Tests handling of invalid updates
- `test_module_import_with_various_environments` - Tests module import under different conditions

## Running Tests

### Prerequisites

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

### Running All Tests

```bash
# Run all tests with verbose output
python -m pytest tests/test_bot.py -v

# Run tests with coverage report
python -m coverage run -m pytest tests/test_bot.py
python -m coverage report --include="bot.py"

# Generate HTML coverage report
python -m coverage html --include="bot.py"
```

### Running Specific Tests

```bash
# Run a specific test class
python -m pytest tests/test_bot.py::TestBotInitialization -v

# Run a specific test method
python -m pytest tests/test_bot.py::TestBotInitialization::test_bot_token_from_env -v
```

## Test Configuration

Tests are configured using:

- `pyproject.toml` - Pytest configuration
- `tests/conftest.py` - Test fixtures and setup
- Environment variable mocking for isolated testing
- Async test support with pytest-asyncio

## Test Coverage

Current test coverage: **94%**

The tests cover:
- ✅ Environment variable loading and validation
- ✅ Bot token handling
- ✅ Start command functionality
- ✅ Application initialization
- ✅ Command handler registration
- ✅ Polling setup
- ✅ Error handling scenarios
- ✅ Integration workflows

## Continuous Testing

To run tests continuously during development:

```bash
# Install pytest-watch
pip install pytest-watch

# Run tests automatically on file changes
ptw tests/test_bot.py
```

## Fixtures

The test suite includes several useful fixtures in `conftest.py`:

- `mock_env_token` - Provides mock BOT_TOKEN environment variable
- `mock_telegram_user` - Creates mock Telegram user objects
- `mock_telegram_chat` - Creates mock Telegram chat objects
- `mock_telegram_message` - Creates mock Telegram message objects
- `mock_telegram_update` - Creates mock Telegram update objects
- `mock_context` - Creates mock context objects
- `clean_environment` - Provides clean environment for testing
- `reset_bot_module` - Automatically resets bot module between tests

## Best Practices

When adding new tests:

1. Use descriptive test names that explain what is being tested
2. Include docstrings for test methods
3. Use appropriate fixtures to reduce code duplication
4. Test both success and failure scenarios
5. Mock external dependencies (Telegram API calls)
6. Test edge cases and error conditions
7. Maintain good test isolation by clearing module cache when needed

## Troubleshooting

Common issues and solutions:

- **Module import errors**: Ensure virtual environment is activated and dependencies installed
- **Test isolation issues**: Tests clear the module cache to ensure proper isolation
- **Async test failures**: Tests use `pytest.mark.asyncio` for async function testing
- **Mock assertion failures**: Verify mock objects are set up correctly and assertions match expected calls