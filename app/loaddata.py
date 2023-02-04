import math
import asyncio
import json
import os
from db import database, metadata, engine, places
from app.core.schemas import PlaceOut

DATA_PATH = os.path.join("core", "data", "places.json")


async def main():
    metadata.create_all(engine)

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
    await database.disconnect() # on conflict postgres


if __name__ == "__main__":
    asyncio.run(main())
