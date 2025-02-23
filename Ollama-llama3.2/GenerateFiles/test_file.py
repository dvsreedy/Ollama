# Testing the regex function with different inputs

import pytest

# Test 1: Basic functionality - Extracting a single email address
def test_extract_email_address():
    text = "Contact me at test@example.com for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 2: Edge case - No email addresses in the text
def test_no_email_addresses():
    text = "This is a sample text without any email addresses."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = []
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 3: Corner case - Single character in the email address
def test_single_character_email_address():
    text = "Contact me at ab.test@example.com for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["ab.test@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 4: Boundary condition - Email address at the start of the text
def test_email_address_at_start():
    text = "Contact me at test@example.com for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 5: Boundary condition - Email address at the end of the text
def test_email_address_at_end():
    text = "Contact me for more information. test@example.com"
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 6: Invalid input - Non-email characters in the text
def test_invalid_input():
    text = "Contact me at test!example.com for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test.example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 7: Empty input - No text to search for email addresses
def test_empty_input():
    text = ""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = []
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 8: Large input - Long text with multiple email addresses
def test_large_input():
    text = "Contact me at test@example.com for more information. You can also reach out to support@anotherdomain.com."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test@example.com", "support@anotherdomain.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 9: Special characters - Email address with special characters
def test_special_characters():
    text = "Contact me at test+info@example.co.uk for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test+info@example.co.uk"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# # Test 10: Unicode characters - Email address with unicode characters
# def test_unicode_characters():
#     text = "Contact me at test�sl�@example.com for more information."
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     expected_output = ["test�sl�@example.com"]
#     assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 11: Case sensitivity - Email address with mixed case
def test_case_sensitivity():
    text = "Contact me at TEST@example.com for more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["TEST@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 12: Multiline input - Email address across multiple lines
def test_multiline_input():
    text = "Contact me at test@example.com\nfor more information."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = ["test@example.com"]
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output

# Test 13: Non-matching scenario - Text with a different format
def test_non_matching_scenario():
    text = "This is a sample text without any email addresses. It has a phone number."
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    expected_output = []
    assert set(pytest.util.re_compile(pattern).findall(text)) == expected_output