# from typing import List, Optional
# from pydantic import BaseModel
# from uuid import UUID

# class UploadResume(BaseModel):
#     uid: UUID
#     user_id: int
#     base_url: str
#     path: int
#     status: int

# class ResumeResponse(UploadResume):
#     uid: UUID

#     class Config:
#         from_attributes = True


from pydantic import BaseModel, UUID4, ConfigDict

class ResumeResponse(BaseModel):
    uid: UUID4
    base_url: str
    path: str
    status: int

    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     orm_mode = True

