import pickle

class Communicator:
    def __init__(self):
        self.outbox = []
        self.inbox = []

    def send_model(self, recipient, model_data):
        package = pickle.dumps(model_data)
        recipient.receive_model(package)

    def receive_model(self, data: bytes):
        model_data = pickle.loads(data)
        self.inbox.append(model_data)

    def fetch_incoming_models(self):
        models = self.inbox[:]
        self.inbox.clear()
        return models
