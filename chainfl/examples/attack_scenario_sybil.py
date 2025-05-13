from chainfl.utils.config_loader import ConfigLoader
from chainfl.blockchain import BlockchainSimulator, ConsensusEngine, LedgerExplorer
from chainfl.coordinator import Aggregator, IntegrityChecker, GlobalPublisher
from chainfl.simulator import SimulationRunner
from chainfl.agent import LocalTrainer, ModelHasher, Signer, Communicator
import numpy as np
from sklearn.datasets import make_classification

# ---------- Custom SybilAgent ----------

class SybilAgent:
    """
    Simulates one malicious agent creating multiple fake identities.
    """
    def __init__(self, true_id, config, n_clones=3):
        self.true_id = true_id
        self.config = config
        self.n_clones = n_clones
        self.clones = self._create_clones()

    def _create_clones(self):
        clones = []
        for i in range(self.n_clones):
            clone_id = self.true_id * 100 + i
            clone = Agent(clone_id, self.config)
            clone.malicious = True
            clones.append(clone)
        return clones

    def get_clones(self):
        return self.clones

# ---------- Standard Agent ----------

class Agent:
    def __init__(self, agent_id, config):
        self.agent_id = agent_id
        self.config = config
        self.X, self.y = self._generate_data()
        self.trainer = LocalTrainer()
        self.hasher = ModelHasher()
        self.signer = Signer()
        self.communicator = Communicator()
        self.consensus = ConsensusEngine(
            mechanism=config['blockchain']['consensus'],
            num_nodes=config['blockchain']['num_nodes'],
            fault_tolerance=config['blockchain']['fault_tolerance']
        )
        self.malicious = False

    def _generate_data(self):
        return make_classification(
            n_samples=self.config['data']['n_samples_per_agent'],
            n_features=self.config['data']['n_features'],
            n_classes=self.config['data']['n_classes'],
            class_sep=self.config['data']['class_sep'],
            random_state=self.agent_id + self.config['data']['random_seed']
        )

    def load_data(self):
        return self.X, self.y

# ---------- Simulation ----------

def main():
    config = ConfigLoader.load("config/default.yaml")
    blockchain = BlockchainSimulator()
    explorer = LedgerExplorer(blockchain)

    # Honest agents
    honest_agents = [Agent(i, config) for i in range(config['experiment']['agents'] - 1)]

    # Sybil attacker with 3 clones
    attacker = SybilAgent(true_id=99, config=config, n_clones=3)
    sybil_clones = attacker.get_clones()

    # Combine agents
    agents = honest_agents + sybil_clones

    # Coordinator
    aggregator = Aggregator(strategy="fedavg")
    checker = IntegrityChecker(blockchain, explorer)
    publisher = GlobalPublisher(blockchain, agents[0].consensus)
    coordinator = type("Coordinator", (), {
        "aggregator": aggregator,
        "publisher": publisher,
        "checker": checker
    })

    # Simulation
    runner = SimulationRunner(
        agents=agents,
        coordinator=coordinator,
        blockchain=blockchain,
        rounds=config['experiment']['rounds']
    )
    runner.run()

    # Summary
    print("\n📘 Final Blockchain Ledger:")
    explorer.print_chain()

    print("\n📉 Sybil attack summary:")
    for clone in sybil_clones:
        blocks = explorer.find_by_agent(clone.agent_id)
        print(f"  - Agent {clone.agent_id}: {len(blocks)} blocks committed")

if __name__ == "__main__":
    main()
