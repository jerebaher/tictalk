from app.config import get_settings

settings = get_settings()

def authenticate_user():
    return "User authenticated"

def create_access_token():
    return "Access token created"

async def get_current_user():
    return "User: UserAuthenticated"