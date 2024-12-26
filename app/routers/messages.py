from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class Message(BaseModel):
    channel: str
    recipient: str
    message: str
    send_time: datetime

@router.post("/messages/schedule")
def schedule_message(msg: Message):
    if msg.send_time <= datetime.now():
        raise HTTPException(status_code=400, detail="La fecha debe ser futura")
    return {"status": "Programado", "channel": msg.channel, "send_time": msg.send_time}
