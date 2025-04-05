
from app.models.jobs import Job
from app.utils.minio import get_minio_obj
from app.models.user_job_status import UserJobStatus
import pandas as pd
import re
from sqlalchemy import text

def matchUserJobs(resume, db):
    userResumeData = get_minio_obj(resume.path)
    # df = pd.read_csv(userResumeData, index_col='Tech Stacks')
    df = pd.read_csv(userResumeData)
    userTechStacks = df['Tech Stacks'][0]
    if userTechStacks is not None:
        userJobStatusArr = []
        userTechStacks = re.split(r',\s*', userTechStacks)
        jobs = db.query(Job).all()
        for job in jobs:
            matching_skills = set(map(str.lower, userTechStacks)) & set(map(str.lower, job.tech_skills))
            matchPercent = 0 if len(matching_skills) == 0 else (len(matching_skills) / len(job.tech_skills)) * 100
            remarks = f"{len(matching_skills)} Matching skills found and {matchPercent}% matching your profile"
            print(remarks)
            userJobStatusObj = UserJobStatus(user_id=resume.user_id, job_id=job.job_id, status=2, remarks=remarks)
            userJobStatusArr.append(userJobStatusObj)
        db.query(UserJobStatus).filter(UserJobStatus.user_id == resume.user_id).delete()
        db.bulk_save_objects(userJobStatusArr)
        db.commit()
        print(userJobStatusArr)
            