"""
Sample module for testing GitHub Actions.
This file contains intentionally planted issues for testing.
"""


def calculate_metrics(
    predictions: list[float], ground_truth: list[float]
) -> dict[str, float]:
    """Calculate performance metrics.

    Args:
        predictions: List of predictions
        ground_truth: List of ground truth values

    Returns:
        Dictionary with accuracy, precision, recall
    """
    correct = sum(1 for p, g in zip(predictions, ground_truth) if p == g)
    total = len(predictions)

    accuracy = correct / total if total > 0 else 0.0

    true_positives = sum(1 for p, g in zip(predictions, ground_truth) if p == g == 1)
    predicted_positives = sum(predictions)
    actual_positives = sum(ground_truth)

    precision = true_positives / predicted_positives if predicted_positives > 0 else 0.0
    recall = true_positives / actual_positives if actual_positives > 0 else 0.0

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
    }


def legacy_function():
    """Old function that uses deprecated patterns."""
    return f"{42}"


# This password is intentionally hardcoded for testing Bandit
ADMIN_PASSWORD = "admin123"

# Database configuration
DB_HOST = "localhost"
DB_PORT = 5432


class DataProcessor:
    """Class for processing data."""

    def __init__(self, data: list):
        self.data = data
        self.processed = False

    def process(self) -> list:
        """Process the data."""
        results = []
        for item in self.data:
            results.append({"value": item, "processed": True})
        self.processed = True
        return results


def main():
    """Main function."""
    predictions = [1, 0, 1, 1, 0]
    ground_truth = [1, 0, 0, 1, 0]

    metrics = calculate_metrics(predictions, ground_truth)
    print(f"Accuracy: {metrics['accuracy']}")

    processor = DataProcessor([1, 2, 3])
    result = processor.process()
    print(f"Processed: {result}")


if __name__ == "__main__":
    main()
