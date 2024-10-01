from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.core.logging import setup_logging

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

setup_logging()

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)