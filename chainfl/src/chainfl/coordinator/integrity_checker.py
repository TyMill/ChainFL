from chainfl.blockchain.model_hasher import ModelHasher

class IntegrityChecker:
    """
    Verifies that local model updates match hashes stored in the blockchain.
    """

    def __init__(self, blockchain, explorer):
        """
        Args:
            blockchain (BlockchainSimulator): The blockchain ledger instance.
            explorer (LedgerExplorer): Explorer for searching the chain.
        """
        self.blockchain = blockchain
        self.explorer = explorer

    def is_model_valid(self, model_hash: str, agent_id: str) -> bool:
        """
        Checks if a given model hash from an agent is stored in the chain.

        Args:
            model_hash (str): Hash of the model.
            agent_id (str): Originating agent's ID.

        Returns:
            bool: True if a matching block exists, False otherwise.
        """
        matches = self.explorer.find_by_agent(agent_id)
        return any(entry["data"].get("model_hash") == model_hash for entry in matches)

    def is_signature_attached(self, agent_id: str) -> bool:
        """
        Checks whether the block contains a signature.

        Args:
            agent_id (str): Agent whose block should include a signature.

        Returns:
            bool: True if signature is found, False otherwise.
        """
        matches = self.explorer.find_by_agent(agent_id)
        return any("signature" in entry["data"] for entry in matches)
