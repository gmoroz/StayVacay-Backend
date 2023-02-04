from sqlalchemy import create_engine, Table, Column, Integer, String, ARRAY, MetaData
from databases import Database

from .core.config import settings

engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
metadata = MetaData()

places = Table(
    "places",
    metadata,
    Column("pk", Integer, primary_key=True),
    Column("title", String(200)),
    Column("description", String(2000)),
    Column("picture_url", String(200)),
    Column("price", Integer),
    Column("country", String(100)),
    Column("city", String(50)),
    Column("features_on", ARRAY(String(100))),
    Column("features_off", ARRAY(String(100))),
)

database = Database(settings.DATABASE_URI)
