import pytest
from chainfl.blockchain import BlockchainSimulator

def test_block_addition():
    bc = BlockchainSimulator()
    data = {"model_hash": "abc123", "agent_id": "test_agent", "signature": "sig"}
    block = bc.add_block(data)
    assert block.data["model_hash"] == "abc123"
    assert block.index == 1
