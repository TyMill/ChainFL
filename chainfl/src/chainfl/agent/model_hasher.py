import hashlib
import numpy as np

class ModelHasher:
    @staticmethod
    def hash_weights(coef, intercept):
        data = np.concatenate([coef.flatten(), intercept.flatten()])
        byte_repr = data.tobytes()
        hash_digest = hashlib.sha256(byte_repr).hexdigest()
        return hash_digest
