import pytest

from chainfl.simulator.scheduler import Scheduler


def make_agents(count):
    return [f"agent_{idx}" for idx in range(count)]


@pytest.mark.parametrize(
    "sample_ratio, expected_first_round",
    [
        (0.4, ["agent_0", "agent_1"]),
        (0.6, ["agent_0", "agent_1", "agent_2"]),
    ],
)
def test_round_robin_selection_wraps_and_preserves_size(sample_ratio, expected_first_round):
    agents = make_agents(5)
    scheduler = Scheduler(mode="round_robin", sample_ratio=sample_ratio)
    k = len(expected_first_round)

    selections = [scheduler.select_agents(agents, round_idx) for round_idx in range(5)]

    # First round should match expected baseline selection
    assert selections[0] == expected_first_round

    # Every round must select exactly k agents
    assert all(len(selection) == k for selection in selections)

    # Verify wrap-around occurs when advancing far enough
    wrap_round = len(agents) // k + 1
    expected_wrap = [agents[(wrap_round * k + offset) % len(agents)] for offset in range(k)]
    assert selections[wrap_round] == expected_wrap
