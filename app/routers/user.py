from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.user_service import UserCreate, register_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)
