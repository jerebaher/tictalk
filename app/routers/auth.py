from fastapi import APIRouter, Depends, HTTPException

import firebase_admin
from firebase_admin import auth, credentials
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth import authenticate_user
from app.config import get_settings
from app.services.user_service import create_user

router = APIRouter()
security = HTTPBearer()
settings = get_settings()

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    if not token or token == "invalid":
        raise HTTPException(status_code=401, detail="Token inválido")

    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login")
def login(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_data = verify_token(token)
    return {"message": "Authenticated", "user": user_data}

@router.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials.credentials)
    return {"message": "Access granted to protected route"}

@router.post("/token")
def login_for_access_token():
    return authenticate_user()


@router.post("/register")
def register_user():
    return create_user()


@router.post("/token")
def login_for_access_token():
    return authenticate_user()
