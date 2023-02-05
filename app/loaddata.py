import asyncio
import json
import os
from pathlib import Path

from core.schemas import PlaceOut
from db import database, engine, metadata, places

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / os.path.join("app", "core", "data", "places.json")


async def is_db_empty() -> bool:
    await database.connect()
    place = await database.fetch_one(places.select())
    await database.disconnect()
    return place is None


async def main():
    metadata.create_all(engine)

    if not await is_db_empty():
        exit(0)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    await database.connect()
    for record in data:
        features_on = record.pop("features_on").split(", ")
        features_off = record.pop("features_off").split(", ")
        place_model = PlaceOut(
            **record,
            features_off=features_off,
            features_on=features_on,
        )
        query = places.insert().values(place_model.dict())
        await database.execute(query)
    await database.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
