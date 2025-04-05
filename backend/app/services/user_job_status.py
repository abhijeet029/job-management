from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from app.models.jobs import Job
from app.models.user_job_status import UserJobStatus
from app.models.resume import Resume
from app.utils.common import matchUserJobs
from app.models.user_job_status import UserJobStatus
import time

def updateUserJobStatus(db: Session, resumeId):
    resumeData = db.query(Resume).filter(Resume.uid == str(resumeId)).first()
    jobs = db.query(Job).all()
    userJobStatusArr = []
    for job in jobs:
        userJobStatusObj = UserJobStatus(user_id=resumeData.user_id, job_id=job.job_id, status=1, remarks=None)
        userJobStatusArr.append(userJobStatusObj)
    db.query(UserJobStatus).filter(UserJobStatus.user_id == resumeData.user_id).delete()
    db.bulk_save_objects(userJobStatusArr)
    db.commit()
    # exit()
    time.sleep(5)
    matchUserJobs(resumeData, db)
    
    # print(allJobs)
    # return db.query(Job).all()
