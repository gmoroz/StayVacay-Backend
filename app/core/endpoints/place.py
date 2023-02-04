from fastapi import APIRouter, status
from ..schemas import PlaceOut
from ...db import places, database

router = APIRouter(tags=["places"])


@router.get("/places/", response_model=list[PlaceOut])
async def get_places():
    query = places.select()
    return await database.fetch_all(query=query)
