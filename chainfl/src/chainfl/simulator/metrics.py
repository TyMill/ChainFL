from sklearn.metrics import accuracy_score, classification_report

class Metrics:
    """
    Computes performance metrics for classification models.
    """

    @staticmethod
    def compute_accuracy(y_true, y_pred):
        """
        Computes simple classification accuracy.

        Args:
            y_true (array): Ground truth labels.
            y_pred (array): Predicted labels.

        Returns:
            float: Accuracy score.
        """
        return accuracy_score(y_true, y_pred)

    @staticmethod
    def compute_classification_report(y_true, y_pred, output_dict=True):
        """
        Computes detailed classification metrics.

        Args:
            y_true (array): Ground truth labels.
            y_pred (array): Predicted labels.
            output_dict (bool): Whether to return as a dictionary.

        Returns:
            dict or str: Classification report in chosen format.
        """
        return classification_report(y_true, y_pred, output_dict=output_dict)
