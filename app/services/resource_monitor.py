import psutil
import GPUtil
from app.services.docker_manager import docker_manager

class ResourceMonitor:
    @staticmethod
    async def get_node_resources(node):
        client = docker_manager._get_client(node)
        
        # Get CPU usage
        cpu_usage = psutil.cpu_percent()
        
        # Get memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        
        # Get GPU usage
        gpus = GPUtil.getGPUs()
        gpu_usage = [{"id": gpu.id, "memory_used": gpu.memoryUsed, "memory_total": gpu.memoryTotal} for gpu in gpus]
        
        return {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "gpu_usage": gpu_usage
        }

resource_monitor = ResourceMonitor()