# test_ghactions/test_pipeline.py


def simple_addition(a, b):
    return a + b


def test_addition_success():
    """Vérifie que l'addition fonctionne pour le pipeline."""
    assert simple_addition(2, 3) == 5


def test_addition_negative():
    """Vérifie les nombres négatifs."""
    assert simple_addition(-1, 1) == 0


def test_environment_variable():
    """Un test qui passera toujours pour valider le lancement."""
    pipeline_active = True
    assert pipeline_active is True
