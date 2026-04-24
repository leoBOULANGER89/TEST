"""
Integration tests for inference pipeline.
"""


def test_inference_imports():
    """Test que les imports nécessaires fonctionnent."""
    import sample_module

    assert sample_module is not None


def test_inference_module_structure():
    """Test la structure du module d'inference."""
    from sample_module import DataProcessor, calculate_metrics

    processor = DataProcessor([1, 2, 3])
    assert hasattr(processor, "process")
    assert hasattr(calculate_metrics, "__call__")


def test_inference_workflow():
    """Test le workflow d'inference complet."""
    from sample_module import DataProcessor, calculate_metrics

    predictions = [1, 0, 1, 1, 0]
    ground_truth = [1, 0, 0, 1, 0]

    metrics = calculate_metrics(predictions, ground_truth)
    assert metrics is not None

    processor = DataProcessor([1, 2, 3])
    result = processor.process()
    assert result is not None


def test_inference_multiple_classes():
    """Test avec plusieurs instances."""
    from sample_module import DataProcessor

    processors = [DataProcessor([i]) for i in range(3)]
    assert len(processors) == 3
    for processor in processors:
        assert processor.process() is not None
