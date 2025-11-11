from typing import Any

from pydantic import BaseModel

from stay_locator.common.utils import LocationType, TransportMode


class Destination(BaseModel):
    location_type: LocationType
    location: Any
    transport_mode: TransportMode
    commute_time: int = 0
    name: str = ""
