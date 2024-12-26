from fastapi import FastAPI
from app.routers import messages

app = FastAPI()
app.include_router(messages.router)

@app.get('/')
def read_root():
    return {'message': 'Hey, here\'s TicTalk!'}