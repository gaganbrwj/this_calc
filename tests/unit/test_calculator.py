"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

import pytest
from src.calculator import add, divide, subtract, multiply, power, square_root


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2


class TestMultiplyDivide:
    """Test multiplication and division operations"""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56

    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4


class TestAdvancedOperations:
    """Test power and square root operations"""

    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers"""
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError"""
        with pytest.raises(
            ValueError, match="Cannot calculate square root of negative"
        ):
            square_root(-4)


# TODO: Students will add TestMultiplyDivide class
