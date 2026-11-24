# Contributing to Social AI Agent Skill

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs
- Open an issue on GitHub
- Include: Python version, OS, error message, steps to reproduce

### Suggesting Features
- Open a GitHub Discussion first
- Describe the use case and expected behavior

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Run the test suite: `pytest tests/`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

### Code Style
- Use `black` for formatting: `black tools/`
- Use `ruff` for linting: `ruff check tools/`
- Write docstrings for all public functions
- Add type hints where possible

### Adding a New Platform
1. Add platform credentials to `configs/platforms.yaml`
2. Add publisher method to `tools/publisher.py`
3. Add platform guide to `platforms/[platform].md`
4. Add platform-specific content rules to `configs/content_rules.yaml`
5. Write tests in `tests/test_publishers.py`
6. Update README.md

### Adding a New AI Agent
1. Create `agents/[agent_name].md` with role, instructions, output schema
2. Add to `SKILL.md` agent roster
3. Update `configs/agents.yaml`
4. Test the agent instructions manually

## Code of Conduct
- Be respectful and inclusive
- No harassment, discrimination, or personal attacks
- Keep discussions constructive

## License
By contributing, you agree that your contributions will be licensed under the MIT License.
