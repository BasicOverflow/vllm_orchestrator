from pydantic import BaseModel
from typing import List, Dict

class ConfigureRequest(BaseModel):
    models: List[str]
    nodes: List[str]

class InferenceRequest(BaseModel):
    model: str
    prompt: str
    parameters: Dict[str, any] = {}

class StatusResponse(BaseModel):
    nodes: Dict[str, Dict[str, any]]
    models: Dict[str, List[str]]
    requests_processed: int