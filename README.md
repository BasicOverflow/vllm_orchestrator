# vLLM Orchestrator/Load Balancer

This project implements a vLLM orchestrator and load balancer for managing distributed inference across multiple nodes.


## Key Components

1. FastAPI Application (app/main.py): Entry point of the application.
2. API Routes (app/api/routes.py): Define endpoints for configuration, inference requests, and system status.
3. Cluster Manager (app/services/cluster_manager.py): Manages vLLM clusters across nodes.
4. Docker Manager (app/services/docker_manager.py): Handles interactions with Docker on remote machines.
5. Load Balancer (app/services/load_balancer.py): Distributes incoming inference requests.
6. Model Manager (app/services/model_manager.py): Tracks running models and their locations.
7. Resource Monitor (app/services/resource_monitor.py): Monitors available resources on each node.

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (see `app/core/config.py` for required variables)
4. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Usage

1. Configure the desired state using the `/configure` endpoint
2. Submit inference requests to the `/inference` endpoint
3. Check system status using the `/status` endpoint