import time
import hashlib

class Block:
    """
    Represents a single block in the blockchain.
    Stores model update metadata along with hash linking.
    """

    def __init__(self, index: int, previous_hash: str, data: dict, timestamp: float = None):
        """
        Initializes a block instance.

        Args:
            index (int): Block number in the chain.
            previous_hash (str): Hash of the previous block.
            data (dict): Payload (e.g., model hash, agent ID, signature).
            timestamp (float, optional): UNIX timestamp of block creation.
        """
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Computes the SHA256 hash of the block’s content.

        Returns:
            str: Hex digest of the hash.
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self) -> dict:
        """
        Converts block attributes to a serializable dictionary.

        Returns:
            dict: Block data as dictionary.
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }
