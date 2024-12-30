from typing import List, Optional, Literal, Union

from fastapi import APIRouter
from pydantic import BaseModel, field_validator, Field, RootModel
from datetime import datetime, timezone

router = APIRouter()

class Message(BaseModel):
    type: Literal["email_message", "text_message"]
    channel: str
    sender: str
    message: str
    tags: Optional[List[str]] = None
    status: str = Field(default="Scheduled")
    send_time: datetime
    deleted: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    deleted_at: datetime = None

    @field_validator("status")
    def validate_status(cls, status):
        if status not in ["Scheduled", "Sent", "Deleted"]:
            raise ValueError("El estado debe ser Programado, Enviado o Eliminado")
        return status

    @field_validator("send_time")
    def validate_send_time(cls, send_time):
        if send_time <= datetime.now(tz=timezone.utc):
            raise ValueError("La fecha debe ser futura")
        return send_time

class GmailMessage(Message):
    type: Literal["email_message"]
    recipient: str
    subject: str
    attachment: Optional[List[str]] = None

class TelegramMessage(Message):
    type: Literal["text_message"]
    phoneNumber: str

@router.post("/messages")
def schedule_message(msg: Message):
    return {
        "status": "Programado",
        "type": msg.type,
        "channel": msg.channel,
        "send_time": msg.send_time
    }
