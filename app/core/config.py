import os
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "StayVacay"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv(
        "BACKEND_CORS_ORIGINS",
        [
            "http://localhost:8000",
            "https://localhost:8000",
            "http://localhost",
            "https://localhost",
        ],
    )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "stayvacay")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "stayvacay")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "stayvacay")
    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
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
