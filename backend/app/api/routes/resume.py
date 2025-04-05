from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume import upload_resume
from app.utils.response import success_response, error_response

router = APIRouter()

@router.post("/upload", response_model=ResumeResponse)
def upload_resume_route(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.content_type.startswith("text/csv"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    resp = upload_resume(file, db)
    # print(ResumeResponse.model_config(resp).model_dump())
    return resp
