from fastapi import APIRouter, HTTPException
from app.api.models import ConfigureRequest, InferenceRequest, StatusResponse
from app.services.cluster_manager import cluster_manager
from app.services.model_manager import model_manager
from app.services.load_balancer import load_balancer

router = APIRouter()

@router.post("/configure")
async def configure_state(config: ConfigureRequest):
    try:
        await cluster_manager.configure(config.models, config.nodes)
        return {"message": "Configuration updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/inference")
async def run_inference(request: InferenceRequest):
    if not model_manager.is_model_available(request.model):
        raise HTTPException(status_code=400, detail="Model not available")
    
    try:
        instance = load_balancer.get_best_instance(request.model)
        result = await instance.generate(request.prompt, **request.parameters)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status", response_model=StatusResponse)
async def get_status():
    return {
        "nodes": cluster_manager.get_nodes_status(),
        "models": model_manager.get_models_status(),
        "requests_processed": load_balancer.get_requests_processed()
    }