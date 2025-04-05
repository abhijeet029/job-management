from sqlalchemy import Column, ForeignKey, SmallInteger, Integer, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class UserJobStatus(Base):
    __tablename__ = "user_job_status"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.job_id", ondelete="CASCADE"), primary_key=True)
    status = Column(SmallInteger, nullable=False)
    remarks = Column(Text, nullable=True)

    # Optional: relationships
    user = relationship("app.models.users.User", back_populates="job_statuses")
    job = relationship("app.models.jobs.Job", back_populates="user_statuses")
