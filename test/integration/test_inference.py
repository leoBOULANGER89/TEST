"""
Integration tests for inference pipeline.
"""


def test_inference_imports():
    """Test que les imports nécessaires fonctionnent."""
    import src.sample_module

    assert src.sample_module is not None


def test_inference_module_structure():
    """Test la structure du module d'inference."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    assert hasattr(instance, "get_info")
    assert hasattr(instance, "process")


def test_inference_workflow():
    """Test le workflow d'inference complet."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    info = instance.get_info()
    assert info is not None
    result = instance.process()
    assert result is not None


def test_inference_multiple_classes():
    """Test avec plusieurs instances."""
    from src.sample_module import SampleClass

    instances = [SampleClass() for _ in range(3)]
    assert len(instances) == 3
    for instance in instances:
        assert instance.get_info() is not None
