import random

class Scheduler:
    """
    Selects which agents participate in each training round.
    Supports random sampling, full participation, and round-robin.
    """

    def __init__(self, mode="random", sample_ratio=1.0):
        """
        Initializes the scheduler.

        Args:
            mode (str): Strategy ('random', 'full', 'round_robin').
            sample_ratio (float): Proportion of agents to select (0.0 - 1.0).
        """
        self.mode = mode
        self.sample_ratio = sample_ratio
        self.round_index = 0

    def select_agents(self, agents: list, current_round: int) -> list:
        """
        Selects a subset of agents for the given round.

        Args:
            agents (list): List of all agent objects.
            current_round (int): Round index.

        Returns:
            list: Selected agents for participation.
        """
        if self.mode == "full":
            return agents

        elif self.mode == "random":
            k = max(1, int(len(agents) * self.sample_ratio))
            return random.sample(agents, k)

        elif self.mode == "round_robin":
            k = max(1, int(len(agents) * self.sample_ratio))
            start = (current_round * k) % len(agents)
            return agents[start:start + k]

        else:
            raise ValueError(f"Unknown scheduling mode: {self.mode}")
