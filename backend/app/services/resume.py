from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.utils.minio import upload_to_minio
from app.models.resume import Resume
from app.utils.response import success_response, error_response
from app.utils.airflow import trigger_airflow_dag

def upload_resume(file: UploadFile, db: Session) -> Resume:
    base_url, path = upload_to_minio(file)
    resume = Resume(
        user_id=1,
        base_url=base_url,
        path=path
    )
    db.add(resume)
    db.commit()
    db.refresh(resume) 
    result = trigger_airflow_dag(resume_id=str(resume.uid))
    if result["success"]:
        print(result["message"])
    else:
        print(result["message"])
        print(result.get("details"))
    resp = success_response(data={}, message="Resume uploaded successfully")
    # print(resp)
    return resp
