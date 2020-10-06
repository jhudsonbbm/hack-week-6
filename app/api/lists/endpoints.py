import app.api.lists.schemas as schemas
import app.api.lists.models as models
from app.api.global_schemas import PydanticOID

from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[schemas.List])
async def get_lists():
    """Return a list of lists."""
    return list(models.List.objects.all())


@router.post("/", response_model=schemas.List)
async def create_list(todo_list: schemas.NewList):
    """Create a new list."""
    return models.List(**todo_list.dict()).save()


@router.patch("/{id}/", response_model=schemas.List)
async def update_list(id: PydanticOID, todo_list: schemas.NewList):
    """Update a list with the given ObjectID"""
    update_dict = todo_list.dict()
    update_dict["id"] = id
    return models.List(**update_dict).save()


@router.delete("/{id}/")
async def delete_list(id: PydanticOID):
    """Delete a list"""
    models.List(id=id).delete()
