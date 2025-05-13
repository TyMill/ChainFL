import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class CryptoUtils:
    """
    Provides basic cryptographic utilities: hashing, key generation, signing.
    """

    @staticmethod
    def generate_key_pair():
        """
        Generates an RSA private/public key pair.

        Returns:
            tuple: (private_key, public_key)
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def sign_message(private_key, message: str) -> bytes:
        """
        Signs a message with a private key.

        Args:
            private_key (RSAPrivateKey): RSA private key.
            message (str): Message to sign.

        Returns:
            bytes: Digital signature.
        """
        return private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    @staticmethod
    def verify_signature(public_key, signature: bytes, message: str) -> bool:
        """
        Verifies the authenticity of a signature.

        Args:
            public_key (RSAPublicKey): RSA public key.
            signature (bytes): Signature to verify.
            message (str): Message that was signed.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

    @staticmethod
    def sha256_from_string(message: str) -> str:
        """
        Computes SHA-256 hash of a string.

        Args:
            message (str): Input string.

        Returns:
            str: Hex digest of SHA-256 hash.
        """
        return hashlib.sha256(message.encode()).hexdigest()
