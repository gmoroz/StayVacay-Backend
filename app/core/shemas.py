from pydantic import BaseModel


class PlaceBase(BaseModel):
    pass  # need to refactor this soon


class PlaceOutDetail(PlaceBase):
    pk: int
    title: str
    description: str
    picture_url: str
    price: int
    country: str
    city: str
    features_on: list[str]
    features_off: list[str]
