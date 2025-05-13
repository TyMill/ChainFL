import random
import time

class ConsensusEngine:
    def __init__(self, mechanism="PBFT", num_nodes=5, fault_tolerance=1):
        """
        :param mechanism: consensus algorithm (currently only PBFT simulated)
        :param num_nodes: number of simulated validators
        :param fault_tolerance: max number of faulty nodes allowed
        """
        self.mechanism = mechanism
        self.num_nodes = num_nodes
        self.fault_tolerance = fault_tolerance
        self.quorum = self.num_nodes - self.fault_tolerance

    def validate_block(self, block_data: dict) -> bool:
        """
        Simulate PBFT consensus by asking all virtual nodes to 'vote'.
        At least quorum nodes must accept the block.
        """
        votes = []

        for i in range(self.num_nodes):
            # Optional logic for faulty node behavior
            if random.random() < 0.05:  # 5% chance node fails
                votes.append(False)
            else:
                votes.append(self.simulate_node_validation(block_data))

        accepted = votes.count(True)
        return accepted >= self.quorum

    def simulate_node_validation(self, block_data: dict) -> bool:
        """
        Each node validates block content (here we simulate logic).
        You can insert realistic validation, e.g., hash format, required fields, timestamp freshness.
        """
        required_fields = ["model_hash", "agent_id", "signature"]
        return all(key in block_data for key in required_fields)

    def simulate_latency(self, min_delay=0.05, max_delay=0.2):
        """
        Simulates network latency for consensus round.
        """
        time.sleep(random.uniform(min_delay, max_delay))
