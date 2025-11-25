from uuid import UUID, uuid4

from sqlmodel import JSON, Column, Enum, Field, SQLModel

from stay_locator.common.utils import LocationType


class Origin(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    # TODO: improve validation
    location: str
    # TODO: break metadata into distinct fields
    origin_metadata: dict = Field(default=None, sa_column=Column(JSON))
    price: float | None = None
    # TODO: Currently has to be coordinates (nearby search)
    location_type: LocationType = Field(sa_column=Column(Enum(LocationType)))
    name: str | None = None
    source_id: str | None = None
    bedrooms: int | None = None
    size: int | None = None
    rating: float | None = None
