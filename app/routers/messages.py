from typing import List, Optional, Literal, Union

from fastapi import APIRouter
from pydantic import BaseModel, field_validator, Field, RootModel
from datetime import datetime

router = APIRouter()

class Message(BaseModel):
    channel: Literal["email", "text_message"]
    sender: str
    message: str
    tags: Optional[List[str]] = None
    status: str = "Scheduled"
    send_time: datetime
    deleted: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime = None

    @field_validator("status")
    def validate_status(self, status):
        if status not in ["Scheduled", "Sent", "Deleted"]:
            raise ValueError("El estado debe ser Programado, Enviado o Eliminado")

    @field_validator("send_time")
    def validate_send_time(self, send_time):
        if send_time <= datetime.now():
            raise ValueError("La fecha debe ser futura")
        return send_time

class GmailMessage(Message):
    type: Literal["Gmail"]
    recipient: str
    subject: str
    attachment: Optional[List[str]] = None

class TelegramMessage(Message):
    type: Literal["text_message"]
    phoneNumber: str

class Message(RootModel[Union[GmailMessage, TelegramMessage]]):
    type_field: str = Field("type", discriminator=True)

@router.post("/messages")
def schedule_message(msg: Message):
    return {"status": "Programado", "channel": msg.channel, "send_time": msg.send_time}
