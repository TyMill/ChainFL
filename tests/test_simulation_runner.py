import numpy as np

from chainfl.simulator.simulation_runner import SimulationRunner
from chainfl.simulator.scheduler import Scheduler


class StubTrainer:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.train_count = 0
        self.set_weights_calls = []

    def train(self, X, y):
        self.train_count += 1

    def get_weights(self):
        # Return deterministic weights per agent so aggregation is stable
        return self.agent_id, float(self.agent_id)

    def set_weights(self, coef, intercept):
        self.set_weights_calls.append((coef, intercept))


class StubHasher:
    def hash_weights(self, coef, intercept):
        return f"{coef}-{intercept}".encode()


class StubSigner:
    def sign(self, message):
        return b"signature"


class StubConsensus:
    def validate_block(self, _block):
        return True

    def simulate_latency(self):
        pass


class StubAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.trainer = StubTrainer(agent_id)
        self.hasher = StubHasher()
        self.signer = StubSigner()
        self.consensus = StubConsensus()

    def load_data(self):
        # Data contents are irrelevant for these tests
        return np.array([self.agent_id]), np.array([self.agent_id])


class StubBlockchain:
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)


class StubPublisher:
    def __init__(self):
        self.published = []

    def publish(self, coef, intercept):
        self.published.append((coef, intercept))


class StubCoordinator:
    def __init__(self):
        self.aggregator = AggregatorSpy()
        self.publisher = StubPublisher()


class AggregatorSpy:
    def __init__(self):
        self.seen_models = []

    def aggregate(self, models):
        self.seen_models.append(models)
        coefs = [coef for coef, _ in models]
        intercepts = [intercept for _, intercept in models]
        return np.mean(coefs, axis=0), np.mean(intercepts, axis=0)


def build_runner(agent_count, rounds, scheduler=None):
    agents = [StubAgent(i) for i in range(agent_count)]
    coordinator = StubCoordinator()
    blockchain = StubBlockchain()
    return SimulationRunner(
        agents=agents,
        coordinator=coordinator,
        blockchain=blockchain,
        rounds=rounds,
        scheduler=scheduler,
    ), agents, coordinator


def test_all_agents_participate_without_scheduler():
    runner, agents, coordinator = build_runner(agent_count=3, rounds=2)

    runner.run()

    # Every agent should have trained once per round
    assert [agent.trainer.train_count for agent in agents] == [2, 2, 2]
    # Aggregator should see contributions from each agent per round
    assert all(len(models) == len(agents) for models in coordinator.aggregator.seen_models)


def test_scheduler_limits_participation_round_robin():
    scheduler = Scheduler(mode="round_robin", sample_ratio=0.5)
    runner, agents, coordinator = build_runner(agent_count=4, rounds=3, scheduler=scheduler)

    runner.run()

    # Round-robin with 4 agents and sample_ratio=0.5 selects 2 agents per round
    assert [agent.trainer.train_count for agent in agents] == [2, 2, 1, 1]
    # Each aggregation should only use the participating subset
    assert all(len(models) == 2 for models in coordinator.aggregator.seen_models)
