from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    uid = Column(String)
    title = Column(String, index=True)
    location = Column(String)
    experience = Column(Integer)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    tech_skills = Column(String)
    jd = Column(String)

    user_statuses = relationship("app.models.user_job_status.UserJobStatus", back_populates="job")

