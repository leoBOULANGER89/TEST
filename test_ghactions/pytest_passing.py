"""
Tests PYTEST qui PASSENT - Tests valides pour GitHub Actions
"""

from lint_without_errors import TestClass as OriginalTestClass
from lint_without_errors import calculate


class TestCalculations:
    """Tests pour les calculs - CES TESTS PASSENT."""

    def test_simple_addition(self):
        """Test addition simple."""
        assert calculate(2, 3) == 5

    def test_negative_numbers(self):
        """Test avec nombres negatifs."""
        assert calculate(-1, 1) == 0

    def test_zero(self):
        """Test avec zero."""
        assert calculate(0, 0) == 0


class TestMyClass:
    """Tests pour la classe - CES TESTS PASSENT."""

    def test_initialization(self):
        """Test initialisation."""
        obj = OriginalTestClass(10)
        assert obj.value == 10

    def test_method(self):
        """Test de la methode."""
        obj = OriginalTestClass(5)
        assert obj.method(1, 2, 3) == 6


def test_function():
    """Test fonction simple."""
    assert True is True
