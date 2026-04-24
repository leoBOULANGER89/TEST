"""
Unit tests for src module.
"""


def test_import_module():
    """Test que le module peut être importé."""
    import src.sample_module

    assert hasattr(src.sample_module, "SampleClass")


def test_sample_class_exists():
    """Test que SampleClass existe."""
    from src.sample_module import SampleClass

    assert SampleClass is not None


def test_sample_class_instantiation():
    """Test instantiation de SampleClass."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    assert instance is not None


def test_sample_class_attributes():
    """Test attributs de SampleClass."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    assert hasattr(instance, "name")
    assert hasattr(instance, "version")


def test_sample_class_methods():
    """Test methodes de SampleClass."""
    from src.sample_module import SampleClass

    instance = SampleClass()
    assert hasattr(instance, "get_info")
    assert hasattr(instance, "process")
