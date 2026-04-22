# Test LINT sans problèmes - CODE PROPRE
# Ce fichier est propre et ne contient pas d'erreurs de linting


def calculate(x: int, y: int) -> int:
    """Calculate sum of two numbers."""
    return x + y


class TestClass:
    """Test class for demonstration."""

    def __init__(self, value: int):
        self.value = value

    def method(self, a: int, b: int, c: int) -> int:
        """Sum three values."""
        return a + b + c


def main():
    """Main function."""
    calc = TestClass(10)
    result = calc.method(1, 2, 3)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
