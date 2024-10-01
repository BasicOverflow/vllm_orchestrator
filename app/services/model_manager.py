class ModelManager:
    def __init__(self):
        self.models = {}

    def add_model_instance(self, model, node, container_id):
        if model not in self.models:
            self.models[model] = []
        self.models[model].append({"node": node, "container_id": container_id})

    def remove_model_instance(self, model, node):
        self.models[model] = [inst for inst in self.models[model] if inst["node"] != node]
        if not self.models[model]:
            del self.models[model]

    def is_model_available(self, model):
        return model in self.models and len(self.models[model]) > 0

    def get_model_instances(self, model):
        return self.models.get(model, [])

    def get_models_status(self):
        return {model: [inst["node"] for inst in instances] for model, instances in self.models.items()}

model_manager = ModelManager()