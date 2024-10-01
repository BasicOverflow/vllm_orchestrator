from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "vLLM Orchestrator"
    PROJECT_VERSION: str = "0.1.0"
    DOCKER_REGISTRY: str = "vllm/vllm-openai"
    DEFAULT_MODEL: str = "facebook/opt-125m"
    
    class Config:
        env_file = ".env"

settings = Settings()