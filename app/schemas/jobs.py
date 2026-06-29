from pydantic import BaseModel, Field

class JobCreate(BaseModel): 
    type: str = Field(..., description="Type of simulation, e.g. wind_analysis")

class JobResponse(BaseModel):
    model_config= {"from_attributes": True}

    id: str
    type: str
    status: str
    created_at: str
    started_at: str | None 
    completed_at: str | None

