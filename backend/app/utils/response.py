# app/utils/response.py

from fastapi.responses import JSONResponse
from app.schemas.response import SuccessResponse, ErrorResponse


def success_response(data: any = None, message: str = "Success", status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content=SuccessResponse(message=message, data=data).dict()
    )


def error_response(message: str, detail: any = None, status_code: int = 400):
    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(message=message, detail=detail).dict()
    )
