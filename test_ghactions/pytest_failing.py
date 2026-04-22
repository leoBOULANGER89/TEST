"""
Tests PYTEST qui ÉCHOUENT - Tests invalides pour GitHub Actions
INTENTIONNEL - Ce test est prévu pour échouer
"""


def test_will_fail():
    """Ce test va échouer."""
    assert 1 == 2, "Ce test échoue intentionnellement"


def test_calculation_error():
    """Erreur de calcul intentionnelle."""
    expected = 10
    actual = 5 + 5  # Cela devrait être 10, donc ce test passe... Changeons
    assert actual == 100, "Ce test échoue car 5+5 != 100"


class TestFailing:
    """Classe de tests qui échouent."""

    def test_method_fail(self):
        """Methode qui echoue."""
        result = 2 + 2
        assert result == 5, "Ce test échoue car 2+2=4"

    def test_another_failure(self):
        """Autre test qui echoue."""
        liste = [1, 2, 3]
        assert len(liste) == 10
