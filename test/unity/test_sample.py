"""
Unit tests for sample_module.
"""


def test_sample_function():
    """Test d'exemple pour fonction simple."""
    assert True


def test_sample_addition():
    """Test d'exemple pour addition."""
    assert 1 + 1 == 2


def test_sample_string():
    """Test d'exemple pour string."""
    result = "eyesdcar"
    assert result == "eyesdcar"
    assert len(result) == 8


def test_sample_list():
    """Test d'exemple pour liste."""
    my_list = [1, 2, 3]
    assert len(my_list) == 3
    assert sum(my_list) == 6
    assert my_list[0] == 1


def test_sample_dict():
    """Test d'exemple pour dictionnaire."""
    config = {"name": "eyesdcar", "version": 1.0}
    assert config["name"] == "eyesdcar"
    assert config["version"] == 1.0
    assert "name" in config


def test_sample_conditional():
    """Test d'exemple pour conditionnelle."""
    value = 10
    if value > 5:
        result = "high"
    else:
        result = "low"
    assert result == "high"


def test_sample_loop():
    """Test d'exemple pour boucle."""
    total = 0
    for i in range(5):
        total += i
    assert total == 10


def test_sample_exception():
    """Test d'exemple pour exception."""
    try:
        raise ValueError("test error")
    except ValueError as e:
        assert str(e) == "test error"


def test_calculate_metrics():
    """Test pour calculate_metrics."""
    from sample_module import calculate_metrics

    predictions = [1, 0, 1, 1, 0]
    ground_truth = [1, 0, 0, 1, 0]

    metrics = calculate_metrics(predictions, ground_truth)
    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert 0.0 <= metrics["accuracy"] <= 1.0


def test_data_processor():
    """Test pour DataProcessor."""
    from sample_module import DataProcessor

    processor = DataProcessor([1, 2, 3])
    assert processor.processed is False
    result = processor.process()
    assert len(result) == 3
    assert processor.processed is True
    assert result[0]["processed"] is True
