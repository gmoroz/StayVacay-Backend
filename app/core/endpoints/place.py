from fastapi import APIRouter, status, HTTPException
from ..schemas import PlaceOut
from ...db import places, database

router = APIRouter(tags=["places"])


@router.get("/places/", response_model=list[PlaceOut])
async def get_places():
    query = places.select()
    return await database.fetch_all(query=query)


@router.get("/places/{pk}", response_model=PlaceOut)
async def get_place(pk: int):
    query = places.select().where(places.c.pk == pk)
    place = await database.fetch_one(query)
    if not place:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Place not found."
        )
    return place
