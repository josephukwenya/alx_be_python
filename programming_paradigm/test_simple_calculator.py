import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  def test_addition(self):
    """Test the addition method."""
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-1, -1), -2)

  def test_subtraction(self):
    """Test the subtraction method."""
    self.assertEqual(self.calc.subtract(5, 3), 2)
    self.assertEqual(self.calc.subtract(-1, 1), -2)
    self.assertEqual(self.calc.subtract(-1, -1), 0)

  def test_multiplication(self):
    """Test the multiplication method."""
    self.assertEqual(self.calc.multiply(2, 3), 6)
    self.assertEqual(self.calc.multiply(-1, 1), -1)
    self.assertEqual(self.calc.multiply(-1, -1), 1)

  def test_division(self):
    """Test the division method."""
    self.assertEqual(self.calc.divide(6, 3), 2)
    self.assertEqual(self.calc.divide(5, 2), 2.5)
    self.assertIsNone(self.calc.divide(5, 0), None)

if __name__ == "__main__":
  unittest.main()