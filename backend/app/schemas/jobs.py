from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID

class JobCreate(BaseModel):
    uid: UUID
    title: str
    location: str
    experience: int
    salary_min: Optional[int]
    salary_max: Optional[int]  # Ensure this is included
    tech_skills: List[str]
    jd: Optional[str]
    remarks: Optional[str]
    status: Optional[str]

class JobResponse(JobCreate):
    uid: UUID

    class Config:
        from_attributes = True
