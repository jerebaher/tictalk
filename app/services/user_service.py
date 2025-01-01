from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from firebase_admin import auth
from pydantic import BaseModel
from fastapi import HTTPException

from app.models.user import User

class UserCreate(BaseModel):
    email: str
    password: str
    name: str

def register_user(db: Session, user_data: UserCreate):
    try:
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password
        )

        new_user = User(
            id=user.uid,
            email=user_data.email,
            name=user_data.name
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User registered successfully", "uid": user.uid}

    except IntegrityError:
        db.rollback()
        auth.delete_user(user.uid)
        raise HTTPException(status_code=400, detail="Email already registered")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
