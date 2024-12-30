from fastapi import FastAPI
from app.routers import messages, config


def create_app() -> FastAPI:
    app = FastAPI()

    # Registrar los routers
    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app


app = create_app()