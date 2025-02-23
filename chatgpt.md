Example-1:
You give short and best practice python code.
Write a python function that uses regex to extract emails
       (including instances of 'name at email dot com') from a text.
      Use pytest to write useful unit tests.

Answer:

Here’s a Python function to extract emails from text, including those in the format `name at email dot com`, and its corresponding pytest unit tests:

### Python Function
```python
import re

def extract_emails(text):
    # Normalize 'name at domain dot com' to 'name@domain.com'
    normalized_text = re.sub(r'\bat\b', '@', re.sub(r'\bdot\b', '.', text, flags=re.IGNORECASE), flags=re.IGNORECASE)
    # Extract valid email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, normalized_text)
```

### Pytest Unit Tests
```python
import pytest
from email_extractor import extract_emails

def test_extract_emails():
    text = """
    Contact us at test.email@gmail.com or admin at example dot com.
    Another email: user123@example.com, or sales at company dot org.
    Invalid: user@@example..com, name.example@.com.
    """
    expected = [
        "test.email@gmail.com",
        "admin@example.com",
        "user123@example.com",
        "sales@company.org",
    ]
    assert extract_emails(text) == expected

def test_empty_text():
    assert extract_emails("") == []

def test_no_emails():
    text = "This is a test with no emails present."
    assert extract_emails(text) == []

def test_edge_cases():
    text = "Mixed format: user.name at domain dot com."
    assert extract_emails(text) == ["user.name@domain.com"]
```

### Key Features
1. **Regex Normalization**: Converts `at` to `@` and `dot` to `.` before extracting emails.
2. **Flexible Matching**: Handles common email formats.
3. **Comprehensive Tests**: Includes typical cases, edge cases, and invalid formats.

Save the function in a file named `email_extractor.py` and run the tests with `pytest`.