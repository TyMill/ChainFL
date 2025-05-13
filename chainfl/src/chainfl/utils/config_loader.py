import yaml

class ConfigLoader:
    """
    Loads experiment configuration from YAML files.
    """

    @staticmethod
    def load(path: str) -> dict:
        """
        Loads YAML config file.

        Args:
            path (str): Path to YAML file.

        Returns:
            dict: Parsed configuration dictionary.
        """
        with open(path, "r") as f:
            return yaml.safe_load(f)
