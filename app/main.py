from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routers import jobs

app = FastAPI(
    title="Simulation Job Queue API",
    description="A job queue API for managing simulation workloads with observability",
    version="2.0.0",
)

Instrumentator().instrument(app).expose(app)

app.include_router(jobs.router)


@app.get("/health")
async def health() -> dict:
    return {"status": "healthy"}