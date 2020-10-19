from typing import Optional
from app.api.lists.schemas import List

from pydantic import BaseModel
from app.api.global_schemas import PydanticOID
from datetime import datetime


class NewItem(BaseModel):
    title: str
    description: Optional[str] = None
    parent: PydanticOID

    class Config:
        title = "Item"
        orm_mode = True
        extra = "ignore"


class UpdateItem(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

    class Config:
        title = "Updated Item"


class Item(NewItem):
    id: PydanticOID
    completed: bool
    created_at: datetime
    parent: PydanticOID