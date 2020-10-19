from typing import List, Optional
import app.api.items.schemas as schemas
import app.api.items.models as models
from app.api.global_schemas import PydanticOID

from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
async def get_items(parent_id: Optional[PydanticOID] = None):
    """Return a list of all items. Optionally search by parent id."""
    items = list(models.Item.objects().all())
    if parent_id:
        items = list(
            filter(
                lambda x: str(x.parent) == parent_id,
                items,
            )
        )
    return items


@router.post("/", response_model=schemas.Item)
async def create_item(item: schemas.NewItem):
    """Create an item"""
    return models.Item(**item.dict()).save()


@router.patch("/{id}/", response_model=schemas.Item)
async def update_item(id: PydanticOID, item: schemas.UpdateItem):
    """Update an item"""
    update_dict = {key:val for (key,val) in item.dict().items() if val}
    item = models.Item.objects.get(id=id)
    item.modify(**update_dict)
    return item.save()


@router.delete("/{id}/")
async def delete_item(id: PydanticOID):
    """Delete an item"""
    models.Item(id=id).delete()