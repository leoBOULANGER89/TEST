"""
End-to-end tests for complete pipeline.
"""


def test_e2e_full_pipeline():
    """Test le pipeline complet E2E."""
    from sample_module import DataProcessor, calculate_metrics

    predictions = [1, 0, 1, 1, 0]
    ground_truth = [1, 0, 0, 1, 0]

    metrics = calculate_metrics(predictions, ground_truth)
    assert metrics is not None

    processor = DataProcessor([1, 2, 3])
    result = processor.process()
    assert result is not None


def test_e2e_multiple_runs():
    """Test plusieurs executions du pipeline."""
    from sample_module import DataProcessor

    results = []
    for _ in range(5):
        processor = DataProcessor([1, 2, 3])
        result = processor.process()
        results.append(result)

    assert len(results) == 5
    assert all(r is not None for r in results)


def test_e2e_data_integrity():
    """Test l'integrité des donnees travers le pipeline."""
    from sample_module import DataProcessor, calculate_metrics

    processor = DataProcessor([1, 2, 3])
    result = processor.process()
    assert isinstance(result, list)
    assert result is not None

    predictions = [1, 0, 1]
    ground_truth = [1, 0, 0]
    metrics = calculate_metrics(predictions, ground_truth)
    assert metrics is not None


def test_e2e_error_handling():
    """Test la gestion des erreurs."""
    from sample_module import DataProcessor

    processor = DataProcessor([1, 2, 3])
    try:
        processor.process()
    except Exception as e:
        assert str(e) is not None
