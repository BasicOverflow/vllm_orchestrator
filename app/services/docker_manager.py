import docker
from app.utils.docker_utils import get_remote_docker_client
from app.core.config import settings

class DockerManager:
    def __init__(self):
        self.clients = {}

    def _get_client(self, node):
        if node not in self.clients:
            self.clients[node] = get_remote_docker_client(node)
        return self.clients[node]

    async def start_vllm_container(self, node, model):
        client = self._get_client(node)
        container = client.containers.run(
            settings.DOCKER_REGISTRY,
            command=f"python -m vllm.entrypoints.openai.api_server --model {model} --host 0.0.0.0 --port 8000",
            detach=True,
            ports={'8000/tcp': None},
            environment={
                "CUDA_VISIBLE_DEVICES": "all"
            },
            gpus='all'
        )
        return container.id

    async def stop_container(self, node, container_id):
        client = self._get_client(node)
        container = client.containers.get(container_id)
        container.stop()
        container.remove()

docker_manager = DockerManager()