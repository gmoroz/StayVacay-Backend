import os
from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator

LOCAL_CORS = [
    "http://localhost:8089",
    "https://localhost:8089",
    "http://localhost:3000",
    "https://localhost:3000",
    "localhost:3000",
    "http://localhost",
    "https://localhost",
]


class Settings(BaseSettings):
    PROJECT_NAME: str = "StayVacay"
    BACKEND_CORS_ORIGINS: str | list[str] = os.getenv(
        "BACKEND_CORS_ORIGINS",
        LOCAL_CORS,
    )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "stayvacay")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "stayvacay")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "stayvacay")
    DATABASE_URI: PostgresDsn | None = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls,
        v: str | None,
        values: dict[str, Any],
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
