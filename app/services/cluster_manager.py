import asyncio
from app.services.docker_manager import docker_manager
from app.services.model_manager import model_manager
from app.core.config import settings

class ClusterManager:
    def __init__(self):
        self.nodes = {}

    async def configure(self, models, nodes):
        # Remove nodes that are no longer in the configuration
        for node in list(self.nodes.keys()):
            if node not in nodes:
                await self._remove_node(node)

        # Add or update nodes
        for node in nodes:
            if node not in self.nodes:
                self.nodes[node] = {"models": []}
            
            # Update models on the node
            current_models = self.nodes[node]["models"]
            models_to_add = [m for m in models if m not in current_models]
            models_to_remove = [m for m in current_models if m not in models]

            for model in models_to_add:
                await self._add_model_to_node(node, model)
            
            for model in models_to_remove:
                await self._remove_model_from_node(node, model)

    async def _add_model_to_node(self, node, model):
        container_id = await docker_manager.start_vllm_container(node, model)
        self.nodes[node]["models"].append(model)
        model_manager.add_model_instance(model, node, container_id)

    async def _remove_model_from_node(self, node, model):
        container_id = model_manager.get_model_instance(model, node)
        await docker_manager.stop_container(node, container_id)
        self.nodes[node]["models"].remove(model)
        model_manager.remove_model_instance(model, node)

    async def _remove_node(self, node):
        for model in self.nodes[node]["models"]:
            await self._remove_model_from_node(node, model)
        del self.nodes[node]

    def get_nodes_status(self):
        return self.nodes

cluster_manager = ClusterManager()