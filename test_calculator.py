import pytest
import math
from calculator import Calculator

class TestCalculator:

    def test_add(self):
        assert Calculator.add(6, 5) == 11.0
        assert Calculator.add(-2, 1) == -1.0
        assert Calculator.add(0, 0) == 0.0

    def test_subtract(self):
        assert Calculator.subtract(3, 2) == 1.0
        assert Calculator.subtract(-2, 1) == -3.0
        assert Calculator.subtract(0, 0) == 0.0

    def test_multiply(self):
        assert Calculator.multiply(2, 3) == 6.0
        assert Calculator.multiply(-2, 1) == -2.0
        assert Calculator.multiply(0, 3) == 0.0

    def test_divide(self):
        assert Calculator.divide(6, 3) == 2.0
        assert Calculator.divide(-6, 3) == -2.0
        with pytest.raises(ValueError, match="Error! Division by zero."):
            Calculator.divide(1, 0)

    def test_power(self):
        assert Calculator.power(2, 3) == 8.0
        assert Calculator.power(2, 0) == 1.0
        assert Calculator.power(2, -2) == 0.25

    def test_square_root(self):
        assert Calculator.square_root(16) == 4.0
        assert Calculator.square_root(0) == 0.0
        with pytest.raises(ValueError, match="Error! Square root of a negative number."):
            Calculator.square_root(-1)

    def test_logarithm(self):
        assert math.isclose(Calculator.logarithm(2), math.log(2), rel_tol=1e-9)
        assert Calculator.logarithm(1) == 0.0
        with pytest.raises(ValueError, match="Error! Logarithm of zero or negative number."):
            Calculator.logarithm(0)
        with pytest.raises(ValueError, match="Error! Logarithm of zero or negative number."):
            Calculator.logarithm(-1)

    def test_factorial(self):
        assert Calculator.factorial(5) == 120.0
        assert Calculator.factorial(0) == 1.0
        assert Calculator.factorial(1) == 1.0
        with pytest.raises(ValueError, match="Error! Factorial of a negative number."):
            Calculator.factorial(-5)
