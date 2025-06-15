# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various numerical inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5)         # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)        # Negative and positive
        self.assertEqual(self.calc.add(-5, -3), -8)       # Negative integers
        self.assertEqual(self.calc.add(0, 0), 0)         # Zeros
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)    # Floats
        self.assertEqual(self.calc.add(100, 0), 100)     # Adding zero
        self.assertEqual(self.calc.add(-7, 0), -7)       # Adding zero to negative

    # RENAMED FROM test_subtract TO test_subtraction to match checker's requirement
    def test_subtraction(self):
        """
        Test the subtract method with various numerical inputs.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)     # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)    # Negative result
        self.assertEqual(self.calc.subtract(-1, 1), -2)   # Negative from negative
        self.assertEqual(self.calc.subtract(1, -1), 2)    # Subtracting a negative
        self.assertEqual(self.calc.subtract(0, 0), 0)     # Zeros
        self.assertEqual(self.calc.subtract(10, 0), 10)   # Subtracting zero
        self.assertEqual(self.calc.subtract(0, 10), -10)  # Subtracting from zero
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0) # Floats

    def test_multiply(self):
        """
        Test the multiply method with various numerical inputs.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)      # Positive integers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative by positive
        self.assertEqual(self.calc.multiply(2, -3), -6)    # Positive by negative
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # Negative by negative
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiply by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)      # Zero by number
        self.assertEqual(self.calc.multiply(0, 0), 0)      # Zeros
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)  # Float by integer
        self.assertEqual(self.calc.multiply(1.5, 1.5), 2.25) # Floats

    def test_divide(self):
        """
        Test the divide method with normal cases and division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)     # Normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)      # Float result
        self.assertEqual(self.calc.divide(-10, 2), -5.0)   # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5.0)   # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5.0)   # Both negative
        self.assertEqual(self.calc.divide(0, 5), 0.0)      # Zero numerator

        # Test division by zero - should return None as per SimpleCalculator's definition
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Still None, as it's a division by zero

if __name__ == '__main__':
    unittest.main()