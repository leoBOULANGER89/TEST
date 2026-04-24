"""
Unit tests for sample_module.
"""


def test_import_module():
    """Test que le module peut être importé."""
    import sample_module

    assert sample_module is not None


def test_calculate_metrics_exists():
    """Test que calculate_metrics existe."""
    from sample_module import calculate_metrics

    assert calculate_metrics is not None


def test_data_processor_exists():
    """Test que DataProcessor existe."""
    from sample_module import DataProcessor

    assert DataProcessor is not None


def test_data_processor_instantiation():
    """Test instantiation de DataProcessor."""
    from sample_module import DataProcessor

    processor = DataProcessor([1, 2, 3])
    assert processor is not None
    assert processor.data == [1, 2, 3]
    assert processor.processed is False


def test_legacy_function():
    """Test legacy_function."""
    from sample_module import legacy_function

    result = legacy_function()
    assert result == "42"
