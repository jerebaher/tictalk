from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

router = APIRouter()
security = HTTPBearer()

@router.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token.get('uid')
        return {"message": "Access granted", "user_id": user_id}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
