import asyncio
from datetime import datetime, timezone
from typing import Dict
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException

from app.models import Job, JobStatus
from app.schemas.jobs import JobCreate, JobResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])

job_store: Dict[UUID, Job] = {}


async def run_job(job_id: UUID) -> None:
    await asyncio.sleep(2)
    job = job_store.get(job_id)
    if not job:
        return
    job.status = JobStatus.RUNNING
    job.started_at = datetime.now(timezone.utc)

    await asyncio.sleep(5)
    job.status = JobStatus.COMPLETED
    job.completed_at = datetime.now(timezone.utc)


@router.post("", response_model=JobResponse, status_code=201)
async def create_job(job_input: JobCreate) -> JobResponse:
    job = Job(type=job_input.type)
    job_store[job.id] = job
    asyncio.create_task(run_job(job.id))
    return JobResponse(
        id=str(job.id),
        type=job.type,
        status=job.status.value,
        created_at=str(job.created_at),
        started_at=None,
        completed_at=None,
    )


@router.get("", response_model=list[JobResponse])
async def list_jobs() -> list[JobResponse]:
    return [
        JobResponse(
            id=str(job.id),
            type=job.type,
            status=job.status.value,
            created_at=str(job.created_at),
            started_at=str(job.started_at) if job.started_at else None,
            completed_at=str(job.completed_at) if job.completed_at else None,
        )
        for job in job_store.values()
    ]


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: UUID) -> JobResponse:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return JobResponse(
        id=str(job.id),
        type=job.type,
        status=job.status.value,
        created_at=str(job.created_at),
        started_at=str(job.started_at) if job.started_at else None,
        completed_at=str(job.completed_at) if job.completed_at else None,
    )