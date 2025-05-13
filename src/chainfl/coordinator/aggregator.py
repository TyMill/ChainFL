import numpy as np

class Aggregator:
    """
    Implements model aggregation strategies for federated learning.
    Default: Federated Averaging (FedAvg).
    """

    def __init__(self, strategy="fedavg"):
        """
        Initializes the aggregator.

        Args:
            strategy (str): Aggregation strategy name.
        """
        self.strategy = strategy

    def aggregate(self, models: list) -> tuple:
        """
        Aggregates model weights using the selected strategy.

        Args:
            models (list): List of tuples (coef, intercept).

        Returns:
            tuple: Aggregated (coef, intercept).
        """
        if not models:
            raise ValueError("No models provided for aggregation.")

        coefs = [m[0] for m in models]
        intercepts = [m[1] for m in models]

        avg_coef = np.mean(coefs, axis=0)
        avg_intercept = np.mean(intercepts, axis=0)

        return avg_coef, avg_intercept
