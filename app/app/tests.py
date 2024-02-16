"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calculator functions in calc.py"""

    def test_add_nums(self):
        """Test adding nums together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_nums(self):
        """Test subtracting nums"""
        res = calc.subtract(3, 8)
        self.assertEqual(res, -5)
