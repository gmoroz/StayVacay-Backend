import asyncio
import json
import os
from pathlib import Path

from core.schemas import PlaceDetail
from db import engine, metadata, places, database


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / os.path.join("app", "core", "data", "places.json")


async def is_db_empty() -> bool:
    async with database:
        place = await database.fetch_one(places.select())
    return place is None


async def main():
    metadata.create_all(engine)

    if not await is_db_empty():
        exit(0)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    async with database:
        for record in data:
            features_on = record.pop("features_on").split(", ")
            features_off = record.pop("features_off").split(", ")
            place_model = PlaceDetail(
                **record,
                features_off=features_off,
                features_on=features_on,
            )
            query = places.insert().values(place_model.dict())
            await database.execute(query)


if __name__ == "__main__":
    asyncio.run(main())
