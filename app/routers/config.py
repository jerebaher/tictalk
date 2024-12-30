from fastapi import APIRouter, Depends
from app.config import get_settings
from app.config import Settings

router = APIRouter()

@router.get("/")
def get_config(settings: Settings = Depends(get_settings)):
    return {"database_url": settings.DATABASE_URL}
