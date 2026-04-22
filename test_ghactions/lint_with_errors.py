# Test LINT avec problèmes - CODE AVEC ERREURS INTENTIONNELLES
# Ce fichier contient des erreurs pour tester les hooks de linting


# Imports non utilisés


def calculate(x, y):
    return x + y


class TestClass:
    def __init__(self):
        self.value = 1

    def method(self, a, b, c):
        return a + b + c


# Variables non utilisées
unused_var = "test"
another_unused = 42
