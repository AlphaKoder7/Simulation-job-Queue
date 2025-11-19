from typing import Dict, List
from uuid import UUID

from fastapi import FastAPI, HTTPException

from app.models import Job, JobCreate

app = FastAPI(
    title="Simulation Job Queue API",
    description="Simple queue API for managing simulation jobs",
    version="0.1.0",
)

job_store: Dict[UUID, Job] = {}


@app.post("/jobs", response_model=Job, status_code=201)
def create_job(job_input: JobCreate) -> Job:
    job = Job(type=job_input.type)
    job_store[job.id] = job
    return job


@app.get("/jobs/{job_id}", response_model=Job)
def get_job(job_id: UUID) -> Job:
    if job_id not in job_store:
        raise HTTPException(status_code=404, detail="Job not found")
    return job_store[job_id]


@app.get("/jobs", response_model=List[Job])
def list_jobs() -> List[Job]:
    return list(job_store.values())


