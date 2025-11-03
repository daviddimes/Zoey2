"""Pytest configuration and fixtures for bot tests."""

import os
import sys
import pytest
from unittest.mock import Mock, AsyncMock, patch

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def mock_env_token():
    """Fixture that provides a mock BOT_TOKEN environment variable."""
    with patch.dict(os.environ, {"BOT_TOKEN": "test_bot_token_123"}):
        yield "test_bot_token_123"


@pytest.fixture
def mock_telegram_user():
    """Fixture that creates a mock Telegram User."""
    user = Mock()
    user.id = 123456789
    user.first_name = "Test"
    user.last_name = "User"
    user.username = "testuser"
    user.is_bot = False
    return user


@pytest.fixture
def mock_telegram_chat():
    """Fixture that creates a mock Telegram Chat."""
    chat = Mock()
    chat.id = 123456789
    chat.type = "private"
    chat.first_name = "Test"
    chat.last_name = "User"
    return chat


@pytest.fixture
def mock_telegram_message(mock_telegram_user, mock_telegram_chat):
    """Fixture that creates a mock Telegram Message."""
    message = AsyncMock()
    message.message_id = 1
    message.from_user = mock_telegram_user
    message.chat = mock_telegram_chat
    message.text = "/start"
    message.date = Mock()
    message.reply_text = AsyncMock()
    return message


@pytest.fixture
def mock_telegram_update(mock_telegram_message):
    """Fixture that creates a mock Telegram Update."""
    update = Mock()
    update.update_id = 123
    update.message = mock_telegram_message
    return update


@pytest.fixture
def mock_context():
    """Fixture that creates a mock Context."""
    return Mock()


@pytest.fixture
def clean_environment():
    """Fixture that provides a clean environment for testing."""
    original_env = os.environ.copy()
    # Clear any existing BOT_TOKEN
    if "BOT_TOKEN" in os.environ:
        del os.environ["BOT_TOKEN"]
    yield
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture(autouse=True)
def reset_bot_module():
    """Automatically reset the bot module before each test."""
    # Remove bot module from sys.modules if it exists
    if "bot" in sys.modules:
        del sys.modules["bot"]
    yield
    # Clean up after test
    if "bot" in sys.modules:
        del sys.modules["bot"]
