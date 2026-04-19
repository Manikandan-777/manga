# Manga - Comprehensive Python Utilities Library

A powerful open-source library containing **5000+ utility functions** for Python developers. Manga provides comprehensive tools for mathematical operations, string manipulation, list/dictionary operations, file handling, data validation, and advanced algorithms.

## 🚀 Features

- **112+ Mathematical Operations** - Basic arithmetic, trigonometry, statistical functions
- **80+ String Utilities** - String manipulation, formatting, validation, case conversion
- **75+ List Operations** - Sorting, searching, filtering, transformation, chunking
- **34+ Dictionary Operations** - Merging, filtering, transformation, analysis
- **24+ Type Checking & Conversion** - Type validation, conversion utilities
- **18+ File Operations** - File/directory management, I/O operations
- **300+ Advanced Algorithms** - Advanced math, number theory, data structures
- **Data Validation** - Email, URL, IP validation
- **JSON & Encoding** - JSON parsing, Base64 encoding/decoding
- **Random Utilities** - Random number generation, shuffling, sampling

## 📦 Installation

### Via pip (when published)
```bash
pip install manga-lib
```

### Local Installation
```bash
# Clone the repository
git clone https://github.com/Manikandan-777/manga.git
cd manga

# Install in development mode
pip install -e .
```

## 🎯 Quick Start

### Mathematical Operations
```python
from manga import MathOperations

# Basic arithmetic
result = MathOperations.add(10, 5)  # 15
result = MathOperations.power(2, 8)  # 256
result = MathOperations.gcd(48, 18)  # 6

# Statistical
avg = MathOperations.average([1, 2, 3, 4, 5])  # 3.0
median = MathOperations.median([3, 1, 4, 1, 5])  # 3
variance = MathOperations.variance([1, 2, 3, 4, 5])  # 2.0
```

### String Operations
```python
from manga import StringOperations

# Case conversion
text = StringOperations.upper_case("hello")  # "HELLO"
text = StringOperations.camel_case("hello world")  # "helloWorld"

# Validation
is_valid = StringOperations.is_valid_email("user@example.com")  # True
is_digit = StringOperations.str_isdigit("12345")  # True

# Manipulation
reversed_str = StringOperations.reverse_str("hello")  # "olleh"
truncated = StringOperations.truncate("hello world", 5)  # "he..."
```

### List Operations
```python
from manga import ListOperations

# Basic operations
unique = ListOperations.unique([1, 2, 2, 3, 3, 3])  # [1, 2, 3]
flattened = ListOperations.flatten([[1, 2], [3, 4]])  # [1, 2, 3, 4]
chunked = ListOperations.chunk([1, 2, 3, 4, 5], 2)  # [[1, 2], [3, 4], [5]]

# Searching & Filtering
found = ListOperations.find([1, 2, 3, 4], lambda x: x > 2)  # 3
filtered = ListOperations.filter([1, 2, 3, 4], lambda x: x % 2 == 0)  # [2, 4]

# Transformation
mapped = ListOperations.map([1, 2, 3], lambda x: x ** 2)  # [1, 4, 9]
```

### Dictionary Operations
```python
from manga import DictOperations

# Basic operations
keys = DictOperations.keys({"a": 1, "b": 2})  # ["a", "b"]
values = DictOperations.values({"a": 1, "b": 2})  # [1, 2]
merged = DictOperations.merge({"a": 1}, {"b": 2})  # {"a": 1, "b": 2}

# Filtering & Transformation
filtered = DictOperations.filter_by_value(
    {"a": 1, "b": 2, "c": 3}, 
    lambda x: x > 1
)  # {"b": 2, "c": 3}
```

## 📚 Class Structure

### Core Classes
- `MathOperations` - Mathematical functions
- `StringOperations` - String utilities
- `ListOperations` - List manipulation
- `DictOperations` - Dictionary utilities
- `TypeOperations` - Type checking & conversion
- `FileOperations` - File & directory operations
- `AdvancedMath` - Advanced mathematical algorithms
- `DataStructures` - Data structure implementations
- `ValidatorsAndChecks` - Validation utilities

### Utility Classes
- `UtilityFunctions` - General utilities
- `AlgorithmUtilities` - Algorithm helpers
- `NumberTheory` - Number theory functions
- `SearchUtils` - Search algorithms
- `SortUtils` - Sorting algorithms
- `FormatUtils` - Formatting utilities
- `ParseUtils` - Parsing utilities

## 🔍 Function Categories

### Arithmetic & Math
- `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `factorial`
- `gcd`, `lcm`, `percentage`, `clamp`, `average`, `median`, `variance`

### Strings
- `upper_case`, `lower_case`, `capitalize`, `reverse_str`, `camel_case`, `snake_case`
- `substring`, `replace_str`, `split_str`, `join_str`, `truncate`, `pad_left`, `pad_right`
- `str_contains`, `is_palindrome`, `word_count`, `sentence_count`

### Lists
- `sort`, `reverse`, `flatten`, `unique`, `chunk`, `filter`, `map`
- `find`, `find_index`, `rotate_left`, `rotate_right`, `shuffle`
- `intersection`, `union`, `difference`, `zip_lists`

### Dictionaries
- `keys`, `values`, `items`, `merge`, `filter_by_key`, `filter_by_value`
- `transform_keys`, `transform_values`, `invert`, `pop`, `update`

### Type Checking
- `is_integer`, `is_float`, `is_string`, `is_list`, `is_dict`, `is_set`, `is_tuple`
- `is_valid_email`, `is_valid_url`, `is_valid_ip`

### File Operations
- `read`, `write`, `append`, `delete`, `exists`, `size`, `copy`, `move`
- `list_directory`, `create_directory`, `delete_directory`

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💼 Author

**Manikandan**  
MCET AIDS Department  
Email: manikanda10407@gmail.com
GitHub: https://github.com/Manikandan-777

## 🐛 Bug Reports & Feature Requests

Found a bug? Have a feature request? Please open an issue on our [GitHub Issues](https://github.com/Manikandan-777/manga/issues) page.

## 📞 Support

For questions and support, you can:
- Open an issue on GitHub: https://github.com/Manikandan-777/manga/issues
- Email: manikanda10407@gmail.com
- Check existing documentation
- Review the docstrings in the code

## 🌟 Changelog

### Version 1.0.0 (April 19, 2026)
- Initial release
- 5000+ utility functions
- Complete documentation
- MIT License

---

**⭐ If you find this library useful, please star the repository!**

