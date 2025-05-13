from chainfl.coordinator import Aggregator
import numpy as np

def test_aggregator_fedavg():
    m1 = (np.ones((1, 5)), np.array([1]))
    m2 = (np.zeros((1, 5)), np.array([0]))
    agg = Aggregator()
    avg_coef, avg_intercept = agg.aggregate([m1, m2])
    assert np.allclose(avg_coef, 0.5)
    assert np.allclose(avg_intercept, 0.5)
