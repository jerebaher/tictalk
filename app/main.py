from fastapi import FastAPI

from app.routers import messages, config, auth

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(messages.router, prefix="/messages")
    app.include_router(config.router, prefix="/config")
    app.include_router(auth.router, prefix="/auth")

    @app.get("/protected")
    def protected_route():
        return {"message": "Ruta protegida"}

    @app.get("/")
    def read_root():
        return {"message": "Hey, here's TicTalk!"}

    return app


app = create_app()