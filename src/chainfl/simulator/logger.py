import json
import os

class Logger:
    """
    Logs simulation results to file for further analysis.
    """

    def __init__(self, path="logs/chainfl_log.json"):
        """
        Args:
            path (str): Path to save logs.
        """
        self.path = path
        self.logs = []

    def log_round(self, round_number, metrics):
        """
        Logs metrics from one round.

        Args:
            round_number (int): Index of the round.
            metrics (dict): Accuracy, hash checks, etc.
        """
        self.logs.append({"round": round_number, **metrics})

    def save(self):
        """
        Saves logs to disk.
        """
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.logs, f, indent=4)
