from fastapi import FastAPI, Depends

from app.routers import messages, config, auth

def create_app() -> FastAPI:
    app = FastAPI(
        description="API para TicTalk",
        title="TicTalk API",
        version="0.1.0"
    )

    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")
    app.include_router(auth.router, prefix="/auth")

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app


app = create_app()