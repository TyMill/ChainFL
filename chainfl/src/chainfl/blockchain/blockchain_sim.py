from .block import Block

class BlockchainSimulator:
    """
    Simulates a simple blockchain ledger for model update registration.
    """

    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the initial genesis block.
        """
        genesis = Block(0, "0", {"genesis": True})
        self.chain.append(genesis)

    def add_block(self, data: dict) -> Block:
        """
        Adds a new block with given data to the blockchain.

        Args:
            data (dict): Model update metadata.

        Returns:
            Block: Newly added block instance.
        """
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            previous_hash=last_block.hash,
            data=data
        )
        self.chain.append(new_block)
        return new_block

    def get_chain(self) -> list:
        """
        Returns the entire blockchain in serializable form.

        Returns:
            list: List of dictionaries representing each block.
        """
        return [block.to_dict() for block in self.chain]
