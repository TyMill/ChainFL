from chainfl.blockchain import ConsensusEngine

def test_consensus_approves_valid_block():
    engine = ConsensusEngine()
    block_data = {"model_hash": "abc", "agent_id": "x", "signature": "sig"}
    assert engine.validate_block(block_data) is True
