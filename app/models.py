from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class JobStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class JobBase(BaseModel):
    type: str = Field(..., description="Type of simulation job, e.g., wind_analysis")


class Job(JobBase):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the job")
    status: JobStatus = Field(
        default=JobStatus.PENDING,
        description="Current lifecycle status for the job",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp indicating when the job was created (UTC)",
    )


class JobCreate(JobBase):
    pass


