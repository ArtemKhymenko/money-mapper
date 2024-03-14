from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class PlaceBase(BaseModel):
    name: str

class PlaceCreate(PlaceBase):
    country_id: int
    supermarket_id: int

class Place(PlaceBase):
    id: int
    
    country_id: int
    supermarket_id: int

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    places: Optional[list[Place]] = []
    class Config:
        orm_model = True

class SupermarketBase(BaseModel):
    name: str

class SupermarketCreate(SupermarketBase):
    pass

class Supermarket(SupermarketBase):
    id: int
    places: Optional[list[Place]] = []

    class Config:
        orm_model = True

