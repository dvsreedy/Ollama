# my_module.py (Example file to test unit test generation)

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Raises ZeroDivisionError if y is 0."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def greet(name):
    """Greets a person."""
    if not isinstance(name, str):
      raise TypeError("Name must be a string")
    return f"Hello, {name}!"

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

class Calculator:
    """A simple calculator class."""

    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, x):
        self.value += x

    def subtract(self, x):
        self.value -= x

    def get_value(self):
        return self.value

# Example of a function with a more complex return type (list)
def process_data(data):
    """Processes a list of numbers, returning a new list with even numbers doubled."""
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    result = []
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("List elements must be numbers.")
        if item % 2 == 0:
            result.append(item * 2)
        else:
            result.append(item)
    return result


# ```python
import unittest
import random

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(0, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

class TestGreetFunction(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, !")
        with self.assertRaises(TypeError):
            greet(123)

class TestFactorialFunction(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(TypeError):
            factorial("abc")
        with self.assertRaises(ValueError):
            factorial(-1)

class TestCalculatorClass(unittest.TestCase):

    def test_calculator(self):
        calc = Calculator()
        self.assertEqual(calc.get_value(), 0)
        calc.add(5)
        self.assertEqual(calc.get_value(), 5)
        calc.subtract(3)
        self.assertEqual(calc.get_value(), 2)

class TestProcessDataFunction(unittest.TestCase):

    def test_process_data(self):
        self.assertEqual(process_data([]), [])
        self.assertEqual(process_data([1, 2, 3, 4]), [1, 4, 3, 8])
        self.assertEqual(process_data([1.5, 2.5, 3.5, 4.5]), [1.5, 5.0, 3.5, 9.0])
        with self.assertRaises(TypeError):
            process_data("abc")
        with self.assertRaises(TypeError):
            process_data([1, 2, 3, "a"])
# ```