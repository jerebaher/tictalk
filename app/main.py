from fastapi import FastAPI, Depends

from app.auth import get_current_user
from app.routers import messages, config, auth


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")
    app.include_router(auth.router, prefix="/auth")

    @app.get("/protected")
    def read_protected_route(current_user: dict = Depends(get_current_user)):
        return {"message": "Tienes acceso a este recurso protegido", "user": current_user}

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app


app = create_app()