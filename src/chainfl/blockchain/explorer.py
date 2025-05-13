class LedgerExplorer:
    """
    Enables search and audit functions for the blockchain ledger.
    """

    def __init__(self, blockchain_simulator):
        """
        Initializes the explorer with a blockchain instance.

        Args:
            blockchain_simulator (BlockchainSimulator): The simulated ledger.
        """
        self.bc = blockchain_simulator

    def find_by_agent(self, agent_id: str) -> list:
        """
        Finds all blocks created by a specific agent.

        Args:
            agent_id (str): ID of the agent.

        Returns:
            list: List of matching block dictionaries.
        """
        return [b.to_dict() for b in self.bc.chain if b.data.get("agent_id") == agent_id]

    def find_by_hash(self, model_hash: str) -> list:
        """
        Finds blocks matching a specific model hash.

        Args:
            model_hash (str): Hash of model weights.

        Returns:
            list: List of matching block dictionaries.
        """
        return [b.to_dict() for b in self.bc.chain if b.data.get("model_hash") == model_hash]

    def print_chain(self):
        """
        Prints the entire blockchain content to stdout.
        """
        for block in self.bc.chain:
            print(block.to_dict())
