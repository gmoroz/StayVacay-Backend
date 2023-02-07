from app.core.schemas import PlaceDetail, PlaceList
from app.db import database, places
from fastapi import APIRouter, HTTPException, Query, status

router = APIRouter(tags=["places"])


@router.get("/places/", response_model=list[PlaceList])
async def get_places(
    city: str | None = None,
    price_from: int | None = Query(default=None, alias="from"),
    price_to: int | None = Query(default=None, alias="to"),
):
    db_query = places.select()

    if city:
        db_query = db_query.where(places.c.city == city)

    if price_from:
        db_query = db_query.where(places.c.price >= price_from)

    if price_to:
        db_query = db_query.where(places.c.price <= price_to)

    return await database.fetch_all(query=db_query)


@router.get("/places/{pk}", response_model=PlaceDetail)
async def get_place(pk: int):
    query = places.select().where(places.c.pk == pk)
    if place := await database.fetch_one(query):
        return place
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Place not found."
    )
