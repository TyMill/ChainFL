from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

class LocalTrainer:
    def __init__(self, model=None):
        self.model = model or LogisticRegression()
        self.history = []

    def train(self, X, y):
        self.model.fit(X, y)
        preds = self.model.predict(X)
        acc = accuracy_score(y, preds)
        self.history.append({'accuracy': acc})
        return self.model

    def get_weights(self):
        return self.model.coef_, self.model.intercept_

    def set_weights(self, coef, intercept):
        self.model.coef_ = coef
        self.model.intercept_ = intercept
