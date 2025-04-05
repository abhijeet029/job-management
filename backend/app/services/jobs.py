from sqlalchemy.orm import Session
from sqlalchemy import and_, case

from app.models.jobs import Job
from app.models.user_job_status import UserJobStatus
# def create_job(db: Session, job: JobCreate):
#     db_job = Job(**job.dict())
#     db.add(db_job)
#     db.commit()
#     db.refresh(db_job)
#     return db_job

def get_jobs(db: Session):
    return  db.query(
        Job.uid,
        Job.title,
        Job.experience,
        Job.salary_max,
        Job.salary_min,
        Job.location,
        Job.tech_skills,
        Job.jd,
        case(
            [
                (UserJobStatus.status == -1, 'Failed'),
                (UserJobStatus.status == 1, 'In progress'),
                (UserJobStatus.status == 2, 'Completed')
            ],
            else_='Pending'
        ).label("status"),
        UserJobStatus.remarks,
    ).outerjoin(
        UserJobStatus,
        and_(
            Job.job_id == UserJobStatus.job_id,
            UserJobStatus.user_id == 1
        )
    ).all()