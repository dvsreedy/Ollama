# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key

GOOGLE_API_KEY='AIzaSyA8Dsecwk_Gt9KS5u4hk9hnw7gx-OoKIHE'
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

import os
import unittest
import ast  # For parsing Python code
# from google.generativeai import genai

# Set your Gemini API key
genai.configure(api_key=GOOGLE_API_KEY)  # Use environment variable

def generate_unit_tests(code_filepath):
    """Generates unit tests for a given Python file using Gemini."""

    try:
        with open(code_filepath, "r") as f:
            code = f.read()


        # Extract function definitions (for better prompting)
        tree = ast.parse(code)
        function_defs = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        function_signatures = [ast.unparse(func).strip() for func in function_defs] # Get function signatures

        prompt = f"""
        ```python
        {code}
        ```

        Write comprehensive unit tests for the Python code above using the `unittest` framework.
        Consider edge cases, boundary conditions, and different input types.  
        For each function:
        * Provide a clear test function name (e.g., `test_function_name`).
        * Include assertions that cover various scenarios.
        * If possible, use parameterized tests for conciseness.
        * Ensure the tests are self-contained and runnable.

        Here are the function signatures for reference:
        {function_signatures}

        Return the unit test code only (no explanations) which can be run directly.  Do not include the original code.
        """

        model = genai.GenerativeModel('gemini-pro')  # Or a suitable model
        response = model.generate_content(prompt)

        if response.text:
            return response.text
        else:
            return None

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def run_unit_tests(test_code):
    """Runs the generated unit tests and returns the results."""
    try:
        # Dynamically execute the generated test code
        loc = {}  # Local namespace for exec
        exec(test_code, globals(), loc)
        test_suite = unittest.TestLoader().loadTestsFromModule(loc['__main__']) # Load the tests
        test_runner = unittest.TextTestRunner() # Run the tests
        result = test_runner.run(test_suite)
        return result

    except Exception as e:
        return f"Error running tests: {e}"


if __name__ == "__main__":
    filepath = input("Enter the path to the Python file: ")  # e.g., my_module.py
    tests = generate_unit_tests(filepath)

    if tests:
        print("\nGenerated Unit Tests:\n", tests)

        # Save the tests to a file (optional but recommended)
        test_filepath = filepath[:-3] + "_test.py"  # e.g., my_module_test.py
        with open(test_filepath, "w") as f:
            f.write(tests)

        run_result = run_unit_tests(tests)
        if hasattr(run_result, 'wasSuccessful'): # Check if run_result has the attribute
          if run_result.wasSuccessful():
              print("\nUnit tests passed!")
          else:
              print("\nUnit tests failed.")
        else:
          print(run_result) # Print the error message

    else:
        print("Failed to generate unit tests.")