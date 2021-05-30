from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_items():
    return [{"name": "Notebook"}, {"name": "Tablet"}]


@router.get("/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
