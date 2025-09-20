import random

from chainfl.blockchain import ConsensusEngine

def test_consensus_approves_valid_block():
    random.seed(57)
    engine = ConsensusEngine()
    block_data = {"model_hash": "abc", "agent_id": "x", "signature": "sig"}
    assert engine.validate_block(block_data) is True


def test_consensus_with_fault_probability_can_reject_block():
    random.seed(57)
    engine = ConsensusEngine(fault_probability=0.05)
    block_data = {"model_hash": "abc", "agent_id": "x", "signature": "sig"}
    assert engine.validate_block(block_data) is False
