from typing import Optional, Any
from pydantic import BaseModel

class SuccessResponse(BaseModel):
    status: str = "success"
    message: Optional[str] = "Request processed successfully"
    data: Optional[Any] = None


class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    detail: Optional[Any] = None
