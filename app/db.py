import sqlalchemy as sq
from databases import Database

from .core.config import settings

engine = sq.create_engine(settings.DATABASE_URI, pool_pre_ping=True)
metadata = sq.MetaData()

places = sq.Table(
    "places",
    metadata,
    sq.Column("pk", sq.Integer, primary_key=True),
    sq.Column("title", sq.String(200)),
    sq.Column("description", sq.String(2000)),
    sq.Column("picture_url", sq.String(200)),
    sq.Column("price", sq.Integer),
    sq.Column("country", sq.String(100)),
    sq.Column("city", sq.String(50)),
    sq.Column("features_on", sq.ARRAY(sq.String(100))),
    sq.Column("features_off", sq.ARRAY(sq.String(100))),
)

database = Database(settings.DATABASE_URI)  # type: ignore
