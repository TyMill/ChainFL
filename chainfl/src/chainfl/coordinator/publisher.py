from chainfl.blockchain.model_hasher import ModelHasher

class GlobalPublisher:
    """
    Publishes the global model to the blockchain with hash and metadata.
    """

    def __init__(self, blockchain, consensus, coordinator_id="coordinator"):
        """
        Args:
            blockchain (BlockchainSimulator): The simulated ledger.
            consensus (ConsensusEngine): The consensus validator.
            coordinator_id (str): Identifier of the central node.
        """
        self.blockchain = blockchain
        self.consensus = consensus
        self.coordinator_id = coordinator_id

    def publish(self, coef, intercept):
        """
        Publishes the global model to the ledger after consensus.

        Args:
            coef (np.array): Model coefficients.
            intercept (np.array): Model intercept.
        """
        model_hash = ModelHasher.hash_weights(coef, intercept)
        data = {
            "model_hash": model_hash,
            "agent_id": self.coordinator_id,
            "signature": "global_model"
        }

        if self.consensus.validate_block(data):
            self.consensus.simulate_latency()
            self.blockchain.add_block(data)
            return model_hash
        else:
            raise RuntimeError("Consensus failed. Block not added.")
