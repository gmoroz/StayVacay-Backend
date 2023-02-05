from fastapi import APIRouter, HTTPException, status

from app.core.schemas import PlaceOut
from app.db import database, places

router = APIRouter(tags=["places"])


@router.get("/places/", response_model=list[PlaceOut])
async def get_places(city: str | None, from_: int | None, to_: int | None):

    db_query = places.select()

    return await database.fetch_all(query=db_query)


@router.get("/places/{pk}", response_model=PlaceOut)
async def get_place(pk: int):
    query = places.select().where(places.c.pk == pk)
    if place := await database.fetch_one(query):
        return place
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Place not found."
    )
