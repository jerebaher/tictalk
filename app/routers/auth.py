from fastapi import APIRouter

from app.auth import authenticate_user
from app.config import get_settings
from app.services.user_service import create_user

router = APIRouter()

settings = get_settings()

@router.post("/token")
def login_for_access_token():
    return authenticate_user()


@router.post("/register")
def register_user():
    return create_user()


@router.post("/token")
def login_for_access_token():
    return authenticate_user()
