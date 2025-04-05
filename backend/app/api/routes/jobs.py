from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.jobs import get_jobs
from app.schemas.jobs import JobCreate, JobResponse
from typing import List

router = APIRouter()

@router.get("/list", response_model=List[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    job_list = get_jobs(db)
    return job_list
