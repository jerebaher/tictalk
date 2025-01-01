from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.services.auth_service import verify_token

router = APIRouter()
security = HTTPBearer()

@router.post("/login")
def login(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_data = verify_token(token)
    return {"message": "Authenticated", "user": user_data}

@router.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials.credentials)
    return {"message": "Access granted to protected route"}
