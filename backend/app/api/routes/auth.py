from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
from app.schemas.auth import LoginSchema, TokenResponse
from app.models.users import User
from app.auth.jwt_handler import create_access_token
from app.core.database import get_db
from app.utils.response import success_response, error_response

router = APIRouter()
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    print(payload)
    if not user or not verify_password(payload.password, user.password):
        return error_response('Invalid Credentials', None, 401)
    else: 
        token = create_access_token(data={"sub": user.email})
        return {"access_token": token}