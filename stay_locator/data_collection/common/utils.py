from datetime import date

from pydantic import BaseModel


class OriginSources(BaseModel):
    airbnb: bool = True
    google_maps: bool = True


class QueryDetails(BaseModel):
    location: str
    checkIn: date
    checkOut: date
    adults: int = 2
    max_price: int | None = None
    search_radius: float = 0.6
