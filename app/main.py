from fastapi import FastAPI

from app.routers import messages, config, auth, user

def create_app() -> FastAPI:
    app = FastAPI(
        description="API para TicTalk",
        title="TicTalk API",
        version="0.1.0"
    )

    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")
    app.include_router(auth.router, prefix="/auth")
    app.include_router(user.router, prefix="/user")

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app

app = create_app()