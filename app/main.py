from app.core.config import settings
from app.core.endpoints import place
from app.db import database, engine, metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        "name": "places",
        "description": "`GET` all places/place by `id`. Filter by `price` (`from`, `to`), or/and `city`.",  # noqa: E501
    },
]


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_tags=tags_metadata,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],  # noqa: E501
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(place.router)
