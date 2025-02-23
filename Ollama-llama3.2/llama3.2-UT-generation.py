# This code when run with ollama running locally, generates test_file.py in generatedFiles.
# And it tests the generated code using python environment locally

from ollama import chat
from ollama import ChatResponse
# from langchain.code_parsers import PythonCodeExtractorParser
import pytest  # Make sure pytest is installed: !pip install pytest
from ollama import chat # Assuming you have this installed

def llm_generate_unit_tests(
        query: str
) -> str:
    """
    Generate unit tests for a hypothetical function that does what is described in `query`.
    """

    unit_test_system_prompt_string = """
    You are a specialized assistant designed to create thorough unit tests for functions involving regular expressions (regex). \
    Your task is to generate comprehensive, self-contained unit tests based on a natural language \
    description of the function's intended behavior.

    Instructions:
    1. Carefully analyze the given description.
    2. Create diverse unit tests that cover all aspects of the function's expected behavior, including:
    - Basic functionality
    - Edge cases
    - Corner cases
    - Boundary conditions
    - Invalid inputs
    - Empty inputs
    - Large inputs
    - Special characters
    - Unicode characters (if applicable)
    - Case sensitivity (if applicable)
    - Multiline inputs (if applicable)
    - Non-matching scenarios
    3. If you need to use a unit test framework, use pytest.
    4. Write individual test functions, not a test class.
    5. Use descriptive test names that clearly indicate the specific scenario being tested.
    6. Include detailed assertions that thoroughly check expected outcomes.
    7. Each assert statement should have a message with the expected output and the observed output.
    8. Do not test input longer than 200 characters.
    9. For regex functions, consider testing:
    - Pattern matching accuracy
    - Capturing groups
    - Non-capturing groups
    - Lookahead and lookbehind assertions
    - Greedy vs. non-greedy quantifiers
    - Character classes and negated character classes
    - Anchors (start, end, word boundaries)
    - Flags (e.g., re.IGNORECASE, re.MULTILINE, re.DOTALL)
    - Escape sequences
    10. Do not write the actual function implementation or code to run the tests.
    11. Write the name of the function you are testing as a comment at the top of the code block (do not write a place holder function).
    12. Generate at least 10-15 diverse tests to ensure comprehensive coverage.

    Provide your response as a Python code block containing only the unit tests. \
    Ensure that the tests are varied and cover a wide range of scenarios to thoroughly validate the regex function.

    Example input: "Create tests for a function that extracts all valid email addresses from a given text."

    Your task is to generate appropriate unit tests based on similar natural language descriptions, \
    focusing on comprehensive testing of regex functionality.
    """

    unit_test_prompt = chat(model='llama3.2', messages=[
        {"role": "system", "content": unit_test_system_prompt_string },
        {"role": "user", "content": "{input}"
    }
    ],
    )

    print(unit_test_prompt.message.content)
    # unit_test_prompt = ChatPromptTemplate.from_messages(
    #     [("system", unit_test_system_prompt_string), ("user", "{input}")]
    # )

    # unit_test_chain = unit_test_prompt | llm | PythonCodeExtractorParser()
    # unit_test_code_as_string = unit_test_chain.invoke({"input": query})
    return unit_test_prompt.message.content


import pytest  # Make sure pytest is installed: !pip install pytest
from ollama import chat # Assuming you have this installed

# ... (your llm_generate_unit_tests function - same as before)

def execute_unit_tests(test_code: str):
    """Executes the generated unit test code using pytest."""

    try:
        # Create a temporary file to store the test code
        with open("test_file.py", "w") as f:
            f.write(test_code)

        # Run pytest on the temporary file
        pytest_result = pytest.main(["test_file.py", "-v"])  # -v for verbose output

        # Capture and print test results
        if pytest_result == pytest.ExitCode.OK:
            print("\nAll tests passed!")
            return True
        else:
            print("\nSome tests failed:")
            return False

    except Exception as e:
        print(f"Error executing tests: {e}")
        return False
    finally:
        # Clean up the temporary file (optional but good practice)
        import os
        # try:
        #     os.remove("test_file.py")
        # except OSError as e:
        #     print(f"Could not delete temporary test file: {e}")



# Example usage:
def main():
    query = "Create tests for a function that extracts all valid email addresses from a given text."
    generated_tests = llm_generate_unit_tests(query)

    if generated_tests:  # Check if the LLM generated tests successfully
        test_result = execute_unit_tests(generated_tests)

        if test_result:
            print("Unit tests execution complete and all tests passed")
        else:
            print("Unit tests execution complete, but some tests failed.")
    else:
        print("Failed to generate unit tests")
main()

# llm_generate_unit_tests("Create tests for a function that extracts all valid email addresses from a given text.")