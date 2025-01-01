from fastapi import HTTPException
from firebase_admin import auth

def verify_token(token: str):
    if not token or token == "invalid":
        raise HTTPException(status_code=401, detail="Token inválido")

    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")