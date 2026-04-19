# Contributing to Manga

Thank you for your interest in contributing to Manga! We welcome contributions from developers of all skill levels.

## How to Contribute

### 1. Report Bugs
If you find a bug, please open an issue on GitHub with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and environment info

### 2. Suggest Features
We love feature suggestions! Open an issue with:
- Clear description of the feature
- Use cases and benefits
- Example code if applicable

### 3. Submit Code

#### Getting Started
1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/manga.git
   cd manga
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes
1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Add tests for new functionality
4. Update documentation as needed
5. Commit with clear, descriptive messages:
   ```bash
   git commit -m "Add: Brief description of changes"
   ```
6. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
7. Open a Pull Request on GitHub

## Code Guidelines

### Style
- Follow PEP 8 conventions
- Use clear, descriptive variable names
- Keep functions focused and single-purpose
- Add docstrings to all functions

### Function Format
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ExceptionType: When this exception occurs
    """
    # Implementation
    pass
```

### Documentation
- Add docstrings to all public functions
- Include examples in docstrings where helpful
- Update README.md for major features
- Keep comments clear and concise

### Testing
- Write tests for new functions
- Ensure existing tests still pass
- Test edge cases and error conditions

## Pull Request Process

1. Ensure your code follows the style guidelines
2. Update documentation and README as needed
3. Provide a clear description of changes in your PR
4. Link any related issues
5. Wait for review and address feedback
6. Once approved, your PR will be merged

## Commit Message Guidelines

- Use imperative mood: "Add feature" not "Added feature"
- Start with a category: Add, Fix, Update, Refactor, Docs, etc.
- Be specific and descriptive
- Keep it concise but informative

Examples:
- `Add: new string manipulation function`
- `Fix: division by zero error in calculate function`
- `Update: improve documentation for list operations`
- `Refactor: optimize matrix operations for performance`

## Areas for Contribution

- New utility functions (math, string, list, dict operations)
- Bug fixes and performance improvements
- Documentation improvements
- Test coverage
- Examples and tutorials
- Translation of documentation

## Questions?

- Open an issue for discussion
- Check existing issues and pull requests
- Review the documentation

## Code of Conduct

- Be respectful and inclusive
- Welcome all contributors
- Provide constructive feedback
- Assume good intentions

## Recognition

All contributors will be recognized in:
- CONTRIBUTORS.md file
- GitHub contributors page
- Project documentation

---

Thank you for contributing to Manga! Your efforts help make this library better for everyone.
