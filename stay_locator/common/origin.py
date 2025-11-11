from dataclasses import field
from typing import Any

# TODO: confirm correct pydantic usage
from pydantic import BaseModel

from stay_locator.common.utils import LocationType


class Origin(BaseModel):
    location: Any
    # TODO: break metadata into distinct fields
    metadata: dict = field(default_factory=dict)
    price: float | None = None
    # TODO: Currently has to be coordinates (nearby search)
    location_type: LocationType = LocationType.coordinates
    name: str | None = None
    id: str | None = None
    bedrooms: int | None = None
    size: int | None = None
    rating: float | None = None
