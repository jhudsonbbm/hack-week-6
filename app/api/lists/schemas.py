from pydantic import BaseModel
from app.api.global_schemas import PydanticOID
from datetime import datetime

class NewList(BaseModel):
    name: str

    class Config:
        title="Item"
        orm_mode=True
        extra="ignore"


class UpdateList(NewList):
    id: PydanticOID

class List(UpdateList):
    created_at: datetime