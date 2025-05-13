class SimulationRunner:
    """
    Runs the ChainFL simulation loop across multiple federated agents.
    """

    def __init__(self, agents, coordinator, blockchain, rounds=5):
        """
        Initializes the simulation environment.

        Args:
            agents (list): List of agent objects.
            coordinator (object): Central aggregation and publishing manager.
            blockchain (BlockchainSimulator): Ledger instance.
            rounds (int): Number of federated training rounds.
        """
        self.agents = agents
        self.coordinator = coordinator
        self.blockchain = blockchain
        self.rounds = rounds
        self.logs = []

    def run(self):
        """
        Executes the simulation over the specified number of rounds.
        """
        for r in range(self.rounds):
            print(f"\n🔄 Round {r+1} ------------------")
            round_models = []

            for agent in self.agents:
                # Local training
                X, y = agent.load_data()
                agent.trainer.train(X, y)

                # Hash model + sign
                coef, intercept = agent.trainer.get_weights()
                model_hash = agent.hasher.hash_weights(coef, intercept)
                signature = agent.signer.sign(model_hash)

                # Log to blockchain
                block_data = {
                    "model_hash": model_hash,
                    "agent_id": agent.agent_id,
                    "signature": signature.hex()
                }
                if agent.consensus.validate_block(block_data):
                    agent.consensus.simulate_latency()
                    self.blockchain.add_block(block_data)
                else:
                    print(f"❌ Agent {agent.agent_id}: Consensus failed")

                # Pass model for aggregation
                round_models.append((coef, intercept))

            # Aggregation + publication
            global_coef, global_intercept = self.coordinator.aggregator.aggregate(round_models)
            self.coordinator.publisher.publish(global_coef, global_intercept)

            # Send global model back to agents
            for agent in self.agents:
                agent.trainer.set_weights(global_coef, global_intercept)
