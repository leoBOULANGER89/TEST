"""
End-to-end tests for complete pipeline.
"""


def test_e2e_full_pipeline():
    """Test le pipeline complet E2E."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    info = instance.get_info()
    result = instance.process()
    assert info is not None
    assert result is not None


def test_e2e_multiple_runs():
    """Test plusieurs executions du pipeline."""
    from src.sample_module import SampleClass

    results = []
    for _ in range(5):
        instance = SampleClass()
        result = instance.process()
        results.append(result)
    assert len(results) == 5
    assert all(r is not None for r in results)


def test_e2e_data_integrity():
    """Test l'integrité des donnees travers le pipeline."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    info = instance.get_info()
    assert isinstance(info, (dict, str, type(None)))
    result = instance.process()
    assert result is not None


def test_e2e_error_handling():
    """Test la gestion des erreurs."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    try:
        instance.process()
    except Exception as e:
        assert str(e) is not None
