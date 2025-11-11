from enum import Enum, unique


@unique
class TransportMode(Enum):
    driving = 1
    walking = 2
    bicycling = 3
    transit = 4


@unique
class LocationType(Enum):
    search = 1
    coordinates = 2
    address = 3
    place_id = 4
