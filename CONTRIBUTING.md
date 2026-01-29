# Contributing to Finance Agent 🤝

Thank you for considering contributing to the Finance Agent project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Code Style Guidelines](#code-style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- PostgreSQL with PgVector extension
- Google AI API key
- Basic understanding of:
  - Python programming
  - FastAPI framework
  - Vector databases
  - Financial markets (for feature contributions)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/finance-agent.git
   cd finance-agent
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/kamaravichow/finance-agent.git
   ```

## Development Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

4. **Initialize knowledge base**
   ```bash
   python sync.py
   ```

5. **Verify installation**
   ```bash
   python main.py
   ```

## Making Changes

### Branch Naming Convention

Use descriptive branch names following this pattern:
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation changes
- `refactor/description` - Code refactoring
- `test/description` - Adding or updating tests

Examples:
- `feature/add-nifty-index-tracking`
- `fix/ticker-format-validation`
- `docs/update-installation-guide`

### Development Workflow

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add comments for complex logic
   - Update documentation as needed

3. **Test your changes**
   ```bash
   python main.py
   # Test the functionality manually
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Keep your branch updated**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### Python Style

Follow PEP 8 guidelines with these specifics:

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Max 100 characters (prefer 80)
- **Imports**: Group in this order:
  1. Standard library
  2. Third-party packages
  3. Local imports
  
  ```python
  import os
  from pathlib import Path
  
  from agno.agent import Agent
  from dotenv import load_dotenv
  
  from local_module import LocalClass
  ```

- **Naming conventions**:
  - Variables and functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

### Code Comments

Add comments for complex functions only. Keep them humanized and clear:

```python
# Good: Explains WHY and adds context
# Process all markdown files in the knowledge directory
# This populates the vector database with embedded content for semantic search
for file in Path("./knowledge").glob("**/*.md"):
    knowledge.add_content(path=file, reader=MarkdownReader())

# Bad: States the obvious
# Loop through files
for file in files:
    process(file)
```

### Agent Instructions

When modifying agent instructions:
- Keep them clear and actionable
- Add comments explaining complex workflows
- Test thoroughly with real queries

## Commit Guidelines

### Commit Message Format

Use conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**

```
feat(agent): add support for commodity trading

- Integrated commodity price APIs
- Added MCX symbol format handling
- Updated agent instructions

Closes #123
```

```
fix(yfinance): correct NSE ticker format validation

The previous regex didn't handle special characters in ticker symbols.
Now supports symbols like M&M.NS correctly.
```

```
docs(readme): update installation instructions

Added troubleshooting section for common PgVector installation issues.
```

## Pull Request Process

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] Comments added for complex functions
- [ ] Documentation updated (README, CONTRIBUTING)
- [ ] Manual testing completed
- [ ] No sensitive data (API keys, passwords) in code
- [ ] `.env.example` updated if new variables added

### Submitting a Pull Request

1. **Push your branch to your fork**
2. **Open a Pull Request** on GitHub
3. **Fill out the PR template** with:
   - Clear description of changes
   - Related issue numbers
   - Testing performed
   - Screenshots (if UI changes)

### PR Title Format

Use the same format as commit messages:
```
feat(scope): brief description
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Related Issues
Fixes #123
Related to #456

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Performed
- [ ] Manual testing completed
- [ ] Tested with real stock queries
- [ ] Verified database connections
- [ ] Checked error handling

## Screenshots (if applicable)
Add screenshots here

## Additional Notes
Any additional context or notes for reviewers
```

### Review Process

- Maintainers will review your PR within a few days
- Address any requested changes
- Once approved, your PR will be merged
- Celebrate your contribution! 🎉

## Reporting Bugs

### Before Reporting

- Check existing issues for duplicates
- Verify it's actually a bug (not expected behavior)
- Test with the latest version

### Bug Report Template

When creating a bug report, include:

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Execute query '...'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Screenshots/Logs**
If applicable, add screenshots or error logs.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.10.0]
- Agent version/commit: [e.g., v1.0.0 or commit hash]

**Additional context**
Any other relevant information.
```

## Suggesting Enhancements

We welcome enhancement suggestions! When suggesting features:

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Use case**
How would this feature be used?

**Additional context**
Screenshots, mockups, or examples.
```

### Types of Contributions Needed

We especially welcome contributions in these areas:

- **New data sources**: Integration with additional financial APIs
- **Enhanced analysis**: More sophisticated analysis tools and indicators
- **Testing**: Unit tests and integration tests
- **Documentation**: Tutorials, examples, and improved guides
- **Knowledge base**: Additional investment lessons and strategies
- **Performance**: Optimization and caching improvements
- **UI/UX**: Better interfaces for interacting with the agent

## Development Best Practices

### Security

- Never commit API keys or credentials
- Always use environment variables for secrets
- Review code for security vulnerabilities
- Validate and sanitize user inputs
- Use parameterized queries for database operations

### Performance

- Cache expensive API calls when possible
- Use efficient data structures
- Profile code for bottlenecks
- Consider memory usage for large datasets

### Documentation

- Update README for user-facing changes
- Add docstrings for complex functions
- Keep CONTRIBUTING.md current
- Document breaking changes clearly

### Testing

While we don't have automated tests yet, please:
- Manually test all changes thoroughly
- Test edge cases and error conditions
- Verify database operations
- Test with real market data

## Questions?

If you have questions about contributing:
- Open a discussion on GitHub
- Review existing issues and PRs
- Check the documentation

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Project documentation
- Release notes for significant contributions

Thank you for contributing to Finance Agent! 🚀📈
