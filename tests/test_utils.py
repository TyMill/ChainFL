from chainfl.utils import CryptoUtils

def test_crypto_hash():
    h1 = CryptoUtils.sha256_from_string("test")
    h2 = CryptoUtils.sha256_from_string("test")
    assert h1 == h2
