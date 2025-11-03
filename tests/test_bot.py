"""Unit tests for the Telegram bot."""

import os
import pytest
import sys
from unittest.mock import AsyncMock, Mock, patch

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestBotInitialization:
    """Test bot initialization and environment variable handling."""

    def test_bot_token_from_env(self):
        """Test that bot token is correctly loaded from environment."""
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token_123"}):
            # Clear the module cache to force reimport
            if "bot" in sys.modules:
                del sys.modules["bot"]

            import bot

            assert bot.BOT_TOKEN == "test_token_123"

    def test_bot_token_missing_raises_error(self):
        """Test that missing BOT_TOKEN raises ValueError."""
        # Clear the module cache
        if "bot" in sys.modules:
            del sys.modules["bot"]

        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(
                ValueError, match="BOT_TOKEN environment variable is not set"
            ):
                import bot  # noqa: F401

    def test_load_dotenv_called(self):
        """Test that load_dotenv is called during module import."""
        # Clear the module cache
        if "bot" in sys.modules:
            del sys.modules["bot"]

        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            with patch("dotenv.load_dotenv") as mock_load_dotenv:
                import bot  # noqa: F401

                mock_load_dotenv.assert_called_once()


class TestStartCommandHandler:
    """Test the /start command handler."""

    @pytest.mark.asyncio
    async def test_start_command_success(self, mock_telegram_update, mock_context):
        """Test successful handling of /start command."""
        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Call the start function
            await bot.start(mock_telegram_update, mock_context)

            # Verify reply_text was called with correct message
            mock_telegram_update.message.reply_text.assert_called_once_with(
                "Hello, I am the PROD bot!"
            )

    @pytest.mark.asyncio
    async def test_start_command_no_message(self, mock_context):
        """Test start command handler when update has no message."""
        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            mock_update = Mock()
            mock_update.message = None

            # Should not raise an exception
            await bot.start(mock_update, mock_context)

    @pytest.mark.asyncio
    async def test_start_command_reply_error_handling(self, mock_context):
        """Test start command handler when reply_text raises an exception."""
        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Create mock objects
            mock_message = AsyncMock()
            mock_message.reply_text = AsyncMock(side_effect=Exception("Network error"))

            mock_update = Mock()
            mock_update.message = mock_message

            # Should raise the exception
            with pytest.raises(Exception, match="Network error"):
                await bot.start(mock_update, mock_context)


class TestMainFunction:
    """Test the main function and application setup."""

    @patch("telegram.ext.Application")
    def test_main_function_creates_application(self, mock_application_class):
        """Test that main function creates Application with correct token."""
        # Setup mocks
        mock_builder = Mock()
        mock_application = Mock()
        mock_builder.token.return_value = mock_builder
        mock_builder.build.return_value = mock_application
        mock_application_class.builder.return_value = mock_builder

        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Call main function
            with patch.object(mock_application, "run_polling") as mock_run_polling:
                bot.main()

            # Verify application was built with correct token
            mock_builder.token.assert_called_once_with("test_token")
            mock_builder.build.assert_called_once()
            mock_run_polling.assert_called_once()

    @patch("telegram.ext.Application")
    def test_main_function_adds_command_handler(self, mock_application_class):
        """Test that main function adds the /start command handler."""
        # Setup mocks
        mock_builder = Mock()
        mock_application = Mock()
        mock_builder.token.return_value = mock_builder
        mock_builder.build.return_value = mock_application
        mock_application_class.builder.return_value = mock_builder

        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Call main function
            with patch.object(mock_application, "run_polling") as mock_run_polling:
                bot.main()

            # Verify command handler was added
            mock_application.add_handler.assert_called_once()
            # Check that a handler was added (we can't easily check the exact type without imports)
            assert mock_application.add_handler.called
            mock_run_polling.assert_called_once()

    @patch("telegram.ext.Application")
    def test_main_function_starts_polling(self, mock_application_class):
        """Test that main function starts polling with correct parameters."""
        # Setup mocks
        mock_builder = Mock()
        mock_application = Mock()
        mock_builder.token.return_value = mock_builder
        mock_builder.build.return_value = mock_application
        mock_application_class.builder.return_value = mock_builder

        # Mock Update.ALL_TYPES
        with patch("telegram.Update") as mock_update_class:
            mock_update_class.ALL_TYPES = "ALL_TYPES_MOCK"

            # Setup the environment and import bot
            with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
                if "bot" in sys.modules:
                    del sys.modules["bot"]
                import bot

                # Call main function
                with patch.object(mock_application, "run_polling") as mock_run_polling:
                    bot.main()

                # Verify polling was started
                mock_run_polling.assert_called_once_with(
                    allowed_updates="ALL_TYPES_MOCK"
                )


class TestIntegration:
    """Integration tests for the bot components."""

    @patch("telegram.ext.Application")
    def test_end_to_end_bot_setup(self, mock_application_class):
        """Test complete bot setup from initialization to ready state."""
        # Setup mocks
        mock_builder = Mock()
        mock_application = Mock()
        mock_builder.token.return_value = mock_builder
        mock_builder.build.return_value = mock_application
        mock_application_class.builder.return_value = mock_builder

        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "integration_test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Verify bot token was loaded
            assert bot.BOT_TOKEN == "integration_test_token"

            # Run main function
            with patch.object(mock_application, "run_polling") as mock_run_polling:
                bot.main()

            # Verify complete setup
            mock_application_class.builder.assert_called_once()
            mock_builder.token.assert_called_once_with("integration_test_token")
            mock_builder.build.assert_called_once()
            mock_application.add_handler.assert_called_once()
            mock_run_polling.assert_called_once()

    @pytest.mark.asyncio
    async def test_start_command_integration(self):
        """Test start command in a more realistic scenario."""
        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            # Create mock objects with realistic attributes
            mock_message = AsyncMock()
            mock_message.reply_text = AsyncMock()

            mock_update = Mock()
            mock_update.message = mock_message

            mock_context = Mock()

            # Execute the start command
            await bot.start(mock_update, mock_context)

            # Verify the response
            mock_message.reply_text.assert_called_once_with("Hello, I am the PROD bot!")


class TestErrorHandling:
    """Test error handling scenarios."""

    @pytest.mark.asyncio
    async def test_start_with_invalid_update(self):
        """Test start command with various invalid update scenarios."""
        # Setup the environment and import bot
        with patch.dict(os.environ, {"BOT_TOKEN": "test_token"}):
            if "bot" in sys.modules:
                del sys.modules["bot"]
            import bot

            mock_context = Mock()

            # Test with None update
            await bot.start(None, mock_context)

            # Test with update that has no message
            mock_update = Mock()
            mock_update.message = None
            await bot.start(mock_update, mock_context)

    def test_module_import_with_various_environments(self):
        """Test module import behavior with different environment setups."""
        test_cases = [
            {"BOT_TOKEN": "valid_token_123"},
            {"BOT_TOKEN": ""},  # Empty token should raise error
        ]

        for env_vars in test_cases:
            # Clear module cache
            if "bot" in sys.modules:
                del sys.modules["bot"]

            with patch.dict(os.environ, env_vars, clear=True):
                if env_vars.get("BOT_TOKEN"):
                    # Should import successfully
                    import bot

                    assert bot.BOT_TOKEN == env_vars["BOT_TOKEN"]
                else:
                    # Should raise ValueError for empty token
                    with pytest.raises(ValueError):
                        import bot
