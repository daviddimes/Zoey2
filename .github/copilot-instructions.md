# Copilot Instructions for Zoey2

## Project Overview

Zoey2 is a Python project repository. When working on this repository, ensure all code follows Python best practices and maintains consistency with the existing codebase.

## Build and Setup

- This is a Python project. Use Python 3.x for development.
- Install dependencies using the appropriate package manager (pip, pipenv, poetry, or uv) based on what's configured in the project.
- If no dependency management is currently set up, prefer using modern Python tools like `uv` or `poetry`.

## Testing

- Write tests for all new features and bug fixes.
- Use pytest as the testing framework if creating new tests.
- Ensure tests are placed in a `tests/` directory or follow the existing test structure.
- Run tests before committing changes.
- Aim for good test coverage on new code.

## Code Quality and Linting

- Follow PEP 8 style guidelines for Python code.
- Use type hints where appropriate to improve code clarity and maintainability.
- If linting tools are configured (e.g., ruff, pylint, flake8), run them before committing.
- Format code consistently - prefer using automated formatters like `black` or `ruff format`.
- Keep code readable and well-documented with docstrings for functions and classes.

## Git and Contribution Guidelines

- Create feature branches for all changes.
- Write clear, descriptive commit messages.
- Open pull requests for all changes using the provided PR template.
- Ensure all checks pass before requesting review.
- Update documentation (README.md, docstrings, etc.) when making relevant changes.

## Project Structure

- Keep the project structure clean and organized.
- Place source code in appropriate directories (e.g., `src/`, or package directories).
- Keep tests separate from source code.
- Configuration files should be at the root or in a dedicated config directory.

## Documentation

- Update README.md when adding new features or changing functionality.
- Include docstrings for all public functions, classes, and modules.
- Use clear, concise language in documentation.
- Include examples in documentation where helpful.

## Security

- Never commit secrets, API keys, or credentials to the repository.
- Use environment variables for sensitive configuration.
- Follow security best practices for Python development.
- Keep dependencies up to date to avoid security vulnerabilities.

## General Principles

- Write clean, maintainable code that follows the DRY (Don't Repeat Yourself) principle.
- Prefer simplicity over complexity.
- Consider edge cases and error handling.
- Make minimal changes to achieve the desired outcome.
- When in doubt, follow existing patterns in the codebase.
