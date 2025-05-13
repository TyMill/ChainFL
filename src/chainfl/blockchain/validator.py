from .block import Block

class BlockValidator:
    """
    Provides validation logic for individual blocks and the entire chain.
    """

    def __init__(self):
        pass

    def is_valid_chain(self, chain: list) -> bool:
        """
        Validates the entire blockchain by checking hash consistency.

        Args:
            chain (list): List of Block instances.

        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(chain)):
            curr = chain[i]
            prev = chain[i - 1]
            if curr.previous_hash != prev.hash:
                return False
            if curr.hash != curr.compute_hash():
                return False
        return True

    def is_valid_block(self, block: Block) -> bool:
        """
        Validates a single block by recomputing its hash.

        Args:
            block (Block): The block to validate.

        Returns:
            bool: True if the hash is correct, False otherwise.
        """
        return block.hash == block.compute_hash()
