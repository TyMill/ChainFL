from chainfl.utils.config_loader import ConfigLoader
from chainfl.blockchain import BlockchainSimulator, ConsensusEngine, LedgerExplorer
from chainfl.coordinator import Aggregator, IntegrityChecker, GlobalPublisher
from chainfl.simulator import SimulationRunner, Scheduler
from chainfl.agent import LocalTrainer, ModelHasher, Signer, Communicator
import numpy as np
from sklearn.datasets import make_classification

# ---------- Step 1: Agent definition ----------

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

# ---------- Step 2: Main simulation logic ----------

def main():
    # Load config
    config = ConfigLoader.load("config/default.yaml")

    # Init blockchain
    blockchain = BlockchainSimulator()
    explorer = LedgerExplorer(blockchain)

    # Init agents
    agents = [Agent(i, config) for i in range(config['experiment']['agents'])]

    # Init coordinator
    aggregator = Aggregator(strategy="fedavg")
    checker = IntegrityChecker(blockchain, explorer)
    publisher = GlobalPublisher(blockchain, agents[0].consensus)  # uses agent[0]'s consensus
    coordinator = type("Coordinator", (), {
        "aggregator": aggregator,
        "publisher": publisher,
        "checker": checker
    })

    # Init scheduler
    scheduler = Scheduler(
        mode=config['experiment']['scheduler_mode'],
        sample_ratio=config['experiment']['agent_sample_ratio']
    )

    # Run simulation
    runner = SimulationRunner(
        agents=agents,
        coordinator=coordinator,
        blockchain=blockchain,
        rounds=config['experiment']['rounds']
    )
    runner.scheduler = scheduler  # inject if needed
    runner.run()

    # Show blockchain
    print("\n📘 Final Blockchain Ledger:")
    explorer.print_chain()

if __name__ == "__main__":
    main()
