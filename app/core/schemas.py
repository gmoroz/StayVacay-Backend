from pydantic import BaseModel


class PlaceBase(BaseModel):
    pk: int
    title: str
    description: str
    picture_url: str
    city: str
    country: str
    price: int


class PlaceList(PlaceBase):
    pass


class PlaceDetail(PlaceBase):
    features_on: list[str]
    features_off: list[str]
    host_name: str
    host_phone: str
    host_location: str
