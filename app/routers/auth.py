from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.auth import authenticate_user
from app.config import get_settings
from app.db import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter()

settings = get_settings()

@router.post("/token")
def login_for_access_token():
    return authenticate_user()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user()


@router.post("/token")
def login_for_access_token(form_data: UserCreate, db: Session = Depends(get_db)):
    return authenticate_user()
