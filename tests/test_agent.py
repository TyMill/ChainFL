import pytest
from chainfl.agent import LocalTrainer, ModelHasher
from sklearn.datasets import make_classification
import numpy as np

def test_local_trainer_fit():
    trainer = LocalTrainer()
    X, y = make_classification(n_samples=100, n_features=10, n_classes=2)
    trainer.train(X, y)
    coef, intercept = trainer.get_weights()
    assert coef.shape[1] == 10

def test_model_hasher_hash():
    coef = np.ones((1, 10))
    intercept = np.array([1.0])
    hash1 = ModelHasher.hash_weights(coef, intercept)
    hash2 = ModelHasher.hash_weights(coef, intercept)
    assert hash1 == hash2
