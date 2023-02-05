from fastapi import APIRouter, HTTPException, Query, status

from app.core.schemas import PlaceOut
from app.db import database, places

router = APIRouter(tags=["places"])


@router.get("/places/", response_model=list[PlaceOut])
async def get_places(
    city: str | None = None,
    price_from: int | None = Query(default=0, alias="from"),
    price_to: int | None = Query(default=None, alias="to"),
):
    db_query = places.select()

    if city is not None:
        db_query = db_query.where(places.c.city == city)

    if price_from is not None:
        db_query = db_query.where(places.c.price >= price_from)

    if price_to is not None:
        db_query = db_query.where(places.c.price <= price_to)

    return await database.fetch_all(query=db_query)


@router.get("/places/{pk}", response_model=PlaceOut)
async def get_place(pk: int):
    query = places.select().where(places.c.pk == pk)
    if place := await database.fetch_one(query):
        return place
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Place not found."
    )
