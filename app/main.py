from fastapi import FastAPI, Depends
from fastapi.security import HTTPAuthorizationCredentials

from app.routers import messages, config, auth
from app.routers.auth import verify_token, security

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")
    app.include_router(auth.router, prefix="/auth")

    @app.get("/protected")
    def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
        verify_token(credentials.credentials)
        return {"message": "Ruta protegida con Firebase"}

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app


app = create_app()