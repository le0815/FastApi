from datetime import datetime

from pydantic import BaseModel

class Channel(BaseModel):
    id: int | None = None
    Name: str

class Account(BaseModel):
    id: int | None = None
    Name: str
    ChannelId: int

class Message(BaseModel):
    id: int | None = None
    AccountId: int
    ChannelId: int
    Msg: str
    # Time: datetime | None = None