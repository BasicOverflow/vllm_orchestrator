import random
from app.services.model_manager import model_manager

class LoadBalancer:
    def __init__(self):
        self.requests_processed = 0

    def get_best_instance(self, model):
        instances = model_manager.get_model_instances(model)
        if not instances:
            raise ValueError(f"No instances available for model {model}")
        
        # For simplicity, we're using random selection here.
        # In a real-world scenario, you'd want to implement a more sophisticated
        # algorithm that takes into account current load, latency, etc.
        return random.choice(instances)

    def get_requests_processed(self):
        return self.requests_processed

load_balancer = LoadBalancer()